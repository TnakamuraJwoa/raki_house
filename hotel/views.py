from django.shortcuts import render

# Create your views here.
from .models import House
from .models import Room, Reserve, Calendar, RFourCalendar
from datetime import date
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from .forms import BoxSearchForm, ReserveConfirmationForm
from django.db.models import Q


class HouseView(LoginRequiredMixin, generic.TemplateView):

    def get(self, request, *args, **kwargs):
        house_data = House.objects.all()

        return render(request, 'house.html', {
            'house_data': house_data,
        })


class RoomView(LoginRequiredMixin, generic.DetailView):
    model = Room
    template_name = 'room.html'


class RoomsView(LoginRequiredMixin, generic.ListView):
    model = Room
    template_name = 'room_list.html'
    paginate_by = 5
    ordering = '-room_number'  # order_by('-title')
    # queryset = Room.objects.filter(house_name_id='1')

    def get_queryset(self):
        in_date = '2022-02-17'
        out_date = '2022-02-19'

        get_house_id = self.request.GET.get('house_number')

        if get_house_id is None:
            house_id = self.request.session['house_id']
        else:
            self.request.session['house_id'] = get_house_id
            house_id = get_house_id

        member_id_id = self.request.user.id
        member_type = self.request.user.member_type

        print(house_id)
        print("member_id_id: %d" % member_id_id)
        print("member_type: %d" % member_type)

        # 使用可能カレンダの件数
        available_cal_cnt = Calendar.objects.filter(date__gte=in_date, date__lte=out_date, used=False, cal_active=True).count()
        #部屋の数
        active_room_cnt = Room.objects.filter(house_name_id=house_id, room_active=True).count()
        # 予約の件数
        reserve_cnt = Room.objects.filter(Q(house_name_id=house_id), Q(room_active=True) | Q(reserve__reserve_date__gte=in_date), Q(reserve__reserve_date__lte=out_date)).select_related().all().count()

        print("使用可能カレンダの件数: %d" % available_cal_cnt)
        print("部屋の数: %d" % active_room_cnt)
        print("予約の件数: %d" % reserve_cnt)

        if (active_room_cnt - reserve_cnt) > available_cal_cnt:
            flg = True
        else:
            if member_type >= 3 and (active_room_cnt - reserve_cnt) >= 1:
                flg = True
            else:
                flg = False


        date = datetime.datetime.now() - datetime.timedelta(days=14)

        if house_id and flg == True:
            queryset = Room.objects.filter(Q(house_name_id=house_id), Q(reserve__reserve_date__isnull=True) | Q(reserve__reserve_date__gt=date)).select_related().all().filter(Q(reserve__reserve_date__gt=out_date) | Q(reserve__reserve_date__lt=in_date) | Q(reserve__reserve_date__isnull=True))
        else:
            queryset = Room.objects.none()

        # print(queryset.query)

        return queryset



    def get_context_data(self, **kwargs):
        self.context = super().get_context_data( **kwargs )
        form = BoxSearchForm()
        # page_title を追加する
        self.context['form'] = form

        return self.context


class ReserveConfirmationView(LoginRequiredMixin, generic.View):

    def post(self, request, *args, **kwargs):
        form = ReserveConfirmationForm(initial={
            'room_name': request.POST['room_name'],
            'room_number': request.POST['room_number'],
            'persons': request.POST['persons'],
            'kids': request.POST['kids'],
            'Double_bed': request.POST['Double_bed'],
            'Queen_bed': request.POST['Queen_bed'],
            'Single_Bed': request.POST['Single_Bed'],
        })

        context = {'form': form}

        return render(request, 'reserve_confirmation.html', context)


class ReserveCreateView(LoginRequiredMixin, generic.View):
    def post(self, request, *args, **kwargs):
        reserve_date = date.today()
        room_number_id = request.POST['room_number']

        profile_content = Reserve(reserve_date=reserve_date, room_number_id=room_number_id)
        profile_content.save()


        return render(request, "reserve_create.html")


class RoomView(LoginRequiredMixin, generic.DetailView):
    model = Room
    template_name = 'room.html'


class ReserveReferenceConfView(LoginRequiredMixin, generic.ListView):
    model = Room
    template_name = 'reserve_reference_conf.html'
    paginate_by = 5
    ordering = '-room_number'  # order_by('-title')
    # queryset = Room.objects.filter(house_name_id='1')

    def get_queryset(self):
        queryset = Room.objects.none()
        return queryset

class MkCalendarView(LoginRequiredMixin, generic.ListView):
    model = RFourCalendar
    template_name = 'mk_calendar.html'