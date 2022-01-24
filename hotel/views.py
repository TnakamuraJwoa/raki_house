from django.shortcuts import render

# Create your views here.
from .models import House
from .models import Room
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddUserForm


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
    paginate_by = 2
    ordering = '-room_number'  # order_by('-title')

    # def get_queryset(self):
    #     room = Room.objects.all().order_by('-room_number')
    #
    #     return room

    def get_context_data(self, **kwargs):
        self.context = super().get_context_data( **kwargs )
        form = AddUserForm()
        # page_title を追加する
        self.context['form'] = form

        return self.context


class ReserveConfirmationView(LoginRequiredMixin, generic.View):

    def post(self, request, *args, **kwargs):
        context = {
            'room_name': request.POST['room_name'],
            'room_number': request.POST['room_number'],
            'persons': request.POST['persons'],
            'kids': request.POST['kids'],
            'Double_bed': request.POST['Double_bed'],
            'Queen_bed': request.POST['Queen_bed'],
            'Single_Bed': request.POST['Single_Bed'],

        }
        return render(request, 'reserve_confirmation.html', context)