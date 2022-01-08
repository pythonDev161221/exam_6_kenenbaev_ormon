from django.shortcuts import render, redirect, get_object_or_404

from .forms import CustomerForm
from .models import Customer

# Create your views here.


def index_view(request):
    form = CustomerForm()
    context = Customer.objects.all().order_by('-create_time')
    return render(request, 'index.html', {'context': context, 'form': form})


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


def update_view(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'GET':
        form = CustomerForm(initial={
            'customer_name': customer.customer_name,
            'customer_email': customer.customer_email,
            'order_text': customer.order_text,
        })
        return render(request, "update_order.html", {'customer': customer, "form": form})
    else:
        form = CustomerForm(data=request.POST)
        if form.is_valid():
            customer.customer_name = request.POST.get('customer_name')
            customer.customer_email = request.POST.get('customer_email')
            customer.order_text = request.POST.get('order_text')
            customer.save()
            return redirect("index_view")
        return render(request, "update_order.html", {'customer': customer, "form": form})


def delete_view(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'GET':
        return render(request, "delete_order.html", {'customer': customer})
    else:
        customer.delete()
        return redirect("index_view")
