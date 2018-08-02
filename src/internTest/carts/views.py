from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import Cart
from shoes.models import Shoe

# Create your views here.
def cart_home(request):
    cart_obj,new_obj = Cart.objects.new_or_get(request)
    shoe = cart_obj.shoes.all()
    total = 0
    for x in shoe:
        total+=x.price
    cart_obj.price = total
    cart_obj.save()
    return render(request,'carts/home.html',{})

def cart_update(request):
    shoe_id = request.POST.get('shoe_id')
    if shoe_id is not None:
        try:
            shoe_obj = Shoe.objects.get(id=product_id)
        except Shoe.DoesNotExist:
            return redirect('cart:home')
    cart_obj,new_obj = Cart.objects.new_or_get(request)
    if shoe_obj in cart_obj.shoes.all():
        cart_obj.shoes.remove(shoe_obj)
    else:
        cart_obj.shoes.add(shoes_obj)

    return redirect('cart:home')

