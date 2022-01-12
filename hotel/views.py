from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.views import generic

# def store(request):
#     return render(request, './store.html')

class IndexView(generic.TemplateView):
    template_name = "store.html"