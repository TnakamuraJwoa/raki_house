import calendar
from django.shortcuts import render
from datetime import datetime as dt

# Create your views here.
from .models import House
from .models import Room, Reserve, RFourCalendar
from datetime import date
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
import time
from .forms import CalendarForm, RoomsForm
from django.db.models import Q

from django.db.models import Max
import math
from django.db.models import OuterRef, Subquery


class HouseView(LoginRequiredMixin, generic.TemplateView):

    def get(self, request, *args, **kwargs):
        house_data = House.objects.all()

        return render(request, 'house.html', {
            'house_data': house_data,
        })


class RoomsView(LoginRequiredMixin, generic.ListView):
    model = Room
    template_name = 'room_list.html'
    paginate_by = 5
    ordering = '-room_number'  # order_by('-title')
    # queryset = Room.objects.filter(house_name_id='1')


    def get_queryset(self):
        # in_date = '2022-02-17'
        # out_date = '2022-02-19'
        #
        # get_house_id = self.request.GET.get('house_number')
        #
        # if get_house_id is None:
        #     house_id = self.request.session['house_id']
        # else:
        #     self.request.session['house_id'] = get_house_id
        #     house_id = get_house_id
        #
        # member_id_id = self.request.user.id
        # member_type = self.request.user.member_type
        #
        # print(house_id)
        # print("member_id_id: %d" % member_id_id)
        # print("member_type: %d" % member_type)
        #
        # # 使用可能カレンダの件数
        # available_cal_cnt = Calendar.objects.filter(date__gte=in_date, date__lte=out_date, used=False, cal_active=True).count()
        # #部屋の数
        # active_room_cnt = Room.objects.filter(house_name_id=house_id, room_active=True).count()
        # # 予約の件数
        # reserve_cnt = Room.objects.filter(Q(house_name_id=house_id), Q(room_active=True) | Q(reserve__check_in_date__gte=in_date), Q(reserve__check_in_date__lte=out_date)).select_related().all().count()
        #
        # print("使用可能カレンダの件数: %d" % available_cal_cnt)
        # print("部屋の数: %d" % active_room_cnt)
        # print("予約の件数: %d" % reserve_cnt)
        #
        # if (active_room_cnt - reserve_cnt) > available_cal_cnt:
        #     flg = True
        # else:
        #     if member_type >= 3 and (active_room_cnt - reserve_cnt) >= 1:
        #         flg = True
        #     else:
        #         flg = False
        #
        #
        # date = datetime.datetime.now() - datetime.timedelta(days=14)
        #
        # if house_id and flg == True:
        #     queryset = Room.objects.filter(Q(house_name_id=house_id), Q(reserve__check_in_date__isnull=True) | Q(reserve__check_in_date__gt=date)).select_related().all().filter(Q(reserve__check_in_date__gt=out_date) | Q(reserve__check_in_date__lt=in_date) | Q(reserve__check_in_date__isnull=True))
        # else:
        #     queryset = Room.objects.none()

        queryset = Room.objects.all()

        return queryset


    def get_context_data(self, **kwargs):
        print("person")
        print(self.request.session.get('session_person'))

        self.context = super().get_context_data( **kwargs )

        initial_values = {'date_field': self.request.session.get('session_date_field'), \
                          'stays': self.request.session.get('session_stays'), \
                          'num_people': self.request.session.get('session_num_people'), \
                          'kids1': self.request.session.get('session_kids1'), \
                          'kids2': self.request.session.get('session_kids2'), \
                          'kids3': self.request.session.get('session_kids3'), \
                          'kids4': self.request.session.get('session_kids4')
                          }
        form = RoomsForm(initial = initial_values)

        # page_title を追加する
        self.context['form'] = form

        return self.context



class ReserveConfirmationView(LoginRequiredMixin, generic.View):

    def post(self, request, *args, **kwargs):

        context = {
            'room_name': request.POST.get('room_name', None),
            'room_number': request.POST.get('room_number', None),
            'room_price': request.POST.get('room_price', None),
            'check_in': request.POST.get('check_in', None),
            'check_out': request.POST.get('check_out', None),
        }


        return render(request, 'reserve_confirmation.html', context)


class ReserveCreateView(LoginRequiredMixin, generic.View):

    def post(self, request, *args, **kwargs):
        check_in_date = request.POST.get('check_in', None)
        check_out_date = request.POST.get('check_out', None)

        check_in_date = dt.strptime(check_in_date, '%Y-%m-%d')
        check_out_date = dt.strptime(check_out_date, '%Y-%m-%d')

        ut = time.time()
        dt_now = datetime.datetime.now()
        # 注文番号の取得
        u_time = math.floor(ut)
        id = self.request.user.id
        # 注文番号の設定
        order_number = str(id) + "-" + str(u_time)
        room_number = request.POST.get('room_number', None)
        representative_name = request.POST.get('representative_name', None)

        profile_content = Reserve(order_number=order_number, Representative_name=representative_name, check_in_date=check_in_date, \
                                  check_out_date=check_out_date, processing_date=dt_now, \
                                  Ticket_number_id='tk-000001', room_number_id=room_number, reserve_status=1, member_id_id=id)
        profile_content.save()


        return render(request, "reserve_create.html")


class RoomView(LoginRequiredMixin, generic.DetailView):
    model = Room
    template_name = 'room.html'

    def get_context_data(self, **kwargs):
        self.request.session['session_date_field'] = self.request.GET.get('date_field', None)
        self.request.session['session_stays'] = self.request.GET.get('stays', None)
        self.request.session['session_num_people'] = self.request.GET.get('num_people', None)
        self.request.session['session_kids1'] = self.request.GET.get('kids1', None)
        self.request.session['session_kids2'] = self.request.GET.get('kids2', None)
        self.request.session['session_kids3'] = self.request.GET.get('kids3', None)
        self.request.session['session_kids4'] = self.request.GET.get('kids4', None)

        stay_date = self.request.GET.get('date_field', None)
        stays = self.request.GET.get('stays', None)

        stay_date = dt.strptime(stay_date, '%Y-%m-%d')
        if stays == "":
            check_out = None
            print(stays)
            print(type(stays))
        else:
            check_out = stay_date + datetime.timedelta(days=int(stays))


        self.context = super().get_context_data(**kwargs)
        self.context['check_in'] = str(stay_date)
        self.context['check_out'] = str(check_out)
        self.context['num_people'] = self.request.GET.get('num_people', None)
        return self.context


class ReserveReferenceConfView(LoginRequiredMixin, generic.ListView):
    model = Room
    template_name = 'reserve_syoukai.html'
    paginate_by = 5
    ordering = '-check_in_date'  # order_by('-title')

    def get_queryset(self):
        # 宿泊完了: 2
        # 予約: 1
        # キャンセル: 0
        status = 1
        id = self.request.user.id
        reserve = Reserve.objects.select_related().all()
        queryset1 = Reserve.objects.filter(member_id_id=id, reserve_status=status).values("order_number").annotate(fav_max=Max('check_in_date'))
        que_order_num = queryset1.values("order_number")
        que_fav_max = queryset1.values("fav_max")
        queryset = reserve.filter(order_number__in=Subquery(que_order_num), check_in_date__in=Subquery(que_fav_max))

        print(queryset.query)
        # print(queryset)
        return queryset


class ReserveConpView(LoginRequiredMixin, generic.ListView):
    model = Room
    template_name = 'reserve_conp.html'
    paginate_by = 5
    ordering = '-check_in_date'  # order_by('-title')

    def get_queryset(self):
        # 宿泊完了: 2
        # 予約: 1
        # キャンセル: 0
        status = 2
        id = self.request.user.id
        reserve = Reserve.objects.all().select_related().all()
        queryset1 = Reserve.objects.filter(member_id_id=id, reserve_status=status).values("order_number").annotate(fav_max=Max('check_in_date'))
        que_order_num = queryset1.values("order_number")
        que_fav_max = queryset1.values("fav_max")
        queryset = reserve.filter(order_number__in=Subquery(que_order_num), check_in_date__in=Subquery(que_fav_max))

        print(queryset.query)
        # print(queryset)
        return queryset



class ReserveCancelView(LoginRequiredMixin, generic.ListView):
    model = Room
    template_name = 'reserve_cancel.html'
    paginate_by = 5
    ordering = '-check_in_date'  # order_by('-title')

    def get_queryset(self):
        # 宿泊完了: 2
        # 予約: 1
        # キャンセル: 0
        status = 0
        id = self.request.user.id
        reserve = Reserve.objects.select_related("room_number")
        queryset1 = Reserve.objects.filter(member_id_id=id, reserve_status=status).values("order_number").annotate(fav_max=Max('check_in_date'))
        que_order_num = queryset1.values("order_number")
        que_fav_max = queryset1.values("fav_max")
        queryset = reserve.filter(order_number__in=Subquery(que_order_num), check_in_date__in=Subquery(que_fav_max))

        print(queryset.query)
        # print(queryset)
        return queryset



class MkCalendarView(LoginRequiredMixin, generic.ListView):
    model = RFourCalendar
    template_name = 'mk_calendar.html'

    def get_queryset(self):
        queryset = RFourCalendar.objects.all().values()

        return queryset

    def get_context_data(self, **kwargs):
        self.context = super().get_context_data( **kwargs )
        form = CalendarForm()
        # page_title を追加する
        self.context['form'] = form

        return self.context


class TreeCalendarView(LoginRequiredMixin, generic.ListView):
    model = RFourCalendar
    template_name = 'tree_calendar.html'


class MyPageView(LoginRequiredMixin, generic.ListView):
    model = RFourCalendar
    template_name = 'my_page.html'

    def get_context_data(self, **kwargs):
        today = datetime.date.today()
        year = today.strftime('%Y')
        day = calendar.monthrange(int(year), 12)[1]

        self.context = super().get_context_data( **kwargs )
        self.context['date'] = str(year) + "-12-" + str(day)

        return self.context


class SelectCreateView(LoginRequiredMixin, generic.TemplateView):

    def get(self, request, *args, **kwargs):
        ticket_data = House.objects.all()

        return render(request, 'select_calender.html', {
            'ticket_data': ticket_data,
        })