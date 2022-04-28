from msilib.schema import tables
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from matplotlib.style import context
from .models import *
from .forms import OrderForm
from django.core.checks import messages
from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate, login, logout
# Create your views here.

def index(request):

    return render(request, 'index.html')

def home(request):
    orders = Order.objects.all()
    tables = Table.objects.all()

    total_tables = tables.count()
    
    total_orders = orders.count()

    served = orders.filter(status='Served').count()

    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'tables':tables, 'total_orders':total_orders, 'served':served, 'pending':pending}

    return render(request, 'dashboard.html', context)

def products(request):
    products = Product.objects.all()

    return render(request, 'products.html', {'products':products})

def table(request, pk_test):
    table = Table.objects.get(id=pk_test)
    
    orders = table.order_set.all()
    
    total_orders = orders.count()

    context = {'table':table, 'orders':orders, 'total_orders':total_orders}

    return render(request, 'customer.html', context)



def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Table, Order, fields=('product', 'status'), extra=10)
    table = Table.objects.get(id=pk)
    #form = OrderForm(initial={'table':table})
    formset = OrderFormSet(queryset=Order.objects.none(), instance=table)
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=table)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset}
    return render(request, 'order_form.html', context)

def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'order_form.html', context)


def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'delete.html', context)


def login_user(request):
    if request.POST:
        table_no = request.POST['table_no']
        zone = request.POST['zone']

        user = authenticate(username=table_no, zone=zone)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index')
        else:
            messages.error(request, 'Invalid table_no or zone!')

        
        print(user)
    context = {}
    return render(request, 'login.html', context)