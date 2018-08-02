from django.db import models
from django.conf import settings
from django.db.models.signals import m2m_changed,pre_save
from shoes.models import Shoe

# Create your models here.

User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
    def new_or_get(self,request):
        cart_id = request.session.get('cart_id',None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            print(cart_id)

            #if request.user.is_authenticated() and cart_obj.user is None:
            cart_obj.user = request.user
            cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj,new_obj

    def new(self,user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user = user_obj)

class Cart(models.Model):
    shoes = models.ManyToManyField(Shoe,blank=True)
    user = models.ForeignKey(User,null = True,blank=True,on_delete=models.CASCADE)
    charges = models.DecimalField(default=1000.1,max_digits=40,decimal_places=2)
    itemcost = models.DecimalField(default=0.00,max_digits=40,decimal_places=2)
    total = models.DecimalField(default=0.00,max_digits=40,decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

def __str__(self):
    return str(self.id)

def m2m_changed_cart_receiver(sender,instance,action,*args,**kwargs):
    if action == 'post_add' or action == 'post_remove'or action == 'post_clear':
        shoes = instance.shoes.all()
        total = 0
        for x in shoes:
            total+=x.price
            if instance.itemcost != total:
                instance.itemcost = total

        instance.save()

m2m_changed.connect(m2m_changed_cart_receiver,sender=Cart.shoes.through)

def pre_save_cart_receiver(sender,instance,*args,**kwargs):
    if instance.itemcost>0:
        instance.total = instance.itemcost + instance.charges
    else:
        instance.total = 0

pre_save.connect(pre_save_cart_receiver,sender = Cart)