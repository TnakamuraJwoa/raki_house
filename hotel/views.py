from django.shortcuts import render

# Create your views here.
from .models import Store
from django.views import generic

class StoreView(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        store_data = Store.objects.all()

        return render(request, 'store.html', {
            'store_data': store_data,
        })