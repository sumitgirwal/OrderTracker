from django.shortcuts import render, HttpResponse
from .models import Dish, Order

# Create your views here.
def index(request):
    dishes = Dish.objects.all()
    return render(request, 'index.html', {'dishes': dishes})

def track_order(request):
    orders = Order.objects.all()
    return render(request, 'track-order.html', {'orders': orders})

def create_order(request, pk):
    dish = Dish.objects.get(pk=pk)
    order = Order(dish=dish) 
    order.save()
    return HttpResponse('<div class="text-success">Your order has been successfully placed.<a href="track_order/">Track your order here.</a></div>')