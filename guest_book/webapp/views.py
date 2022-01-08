from django.shortcuts import render

from .models import Customer

# Create your views here.


def index_view(request):
    return render(request, 'index.html', {'context': Customer.objects.all().order_by('-create_time')})

def create_view(request):
    pass

def update_view(request):
    pass
