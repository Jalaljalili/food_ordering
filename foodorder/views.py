from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from .models import Menu, Order
from django.http import HttpResponse
import csv

@login_required
def order_food(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, day_of_week=request.POST.get('day_of_week'))
        if form.is_valid():
            menu_item = form.cleaned_data['food_item']
            Order.objects.create(user=request.user, menu=menu_item)
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'order_food.html', {'form': form})

def order_success(request):
    return render(request, 'order_success.html')

def export_orders(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orders.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'Food Item', 'Order Date'])

    orders = Order.objects.all()
    for order in orders:
        writer.writerow([order.user.username, order.menu.food_item, order.order_date])

    return response

# from django.shortcuts import render

# # Create your views here.
