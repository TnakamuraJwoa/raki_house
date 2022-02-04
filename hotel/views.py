from django.shortcuts import render

# Create your views here.
from .models import House
from .models import Room, Reserve
from datetime import date
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddUserForm, ReserveConfirmationForm


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
        q_word = self.request.GET.get('house_number')

        if q_word:
            object_list = Room.objects.filter(house_name_id=q_word)
        else:
            object_list = Room.objects.all()
        return object_list

    def get_context_data(self, **kwargs):
        self.context = super().get_context_data( **kwargs )
        form = AddUserForm()
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