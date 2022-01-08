from django.shortcuts import render, redirect

from .forms import CustomerForm
from .models import Customer

# Create your views here.


def index_view(request):
    return render(request, 'index.html', {'context': Customer.objects.all().order_by('-create_time')})


def create_view(request):
    if request.method == 'GET':
        form = CustomerForm()
        return render(request, "create_order.html", {'form': form})
    else:
        form = CustomerForm(data=request.POST)
        if form.is_valid():
            customer_name = request.POST.get('customer_name')
            customer_email = request.POST.get('customer_email')
            order_text = request.POST.get('order_text')
            order = Customer(customer_name=customer_name, customer_email=customer_email,
                             order_text=order_text)
            order.save()
            return redirect('index_view')
        return render(request, "create_order.html", {'form': form})

def update_view(request):
    pass
