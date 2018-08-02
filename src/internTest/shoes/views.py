from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from django.http import Http404
from .models import Shoe
from carts.models import Cart
# Create your views here.


class shoeListView(ListView):
    queryset = Shoe.objects.all()
    template_name = 'shoes/list.html' 

    def get_context_data(self,*args,**kwargs):
        context = super(shoeListView,self).get_context_data(*args,**kwargs)
        print(context)
        return context

class shoeDetailView(DetailView):
    queryset = Shoe.objects.all()
    template_name = 'shoes/detail.html'

    def get_context_data(self,*args,**kwargs):
        context = super(shoeDetailView,self).get_context_data(*args,**kwargs)
        return context


class shoeSlugDetailView(DetailView):
    queryset = Shoe.objects.all()
    template_name = 'shoes/detail.html'

    def get_context_data(self,*args,**kwargs):
        context = super(shoeSlugDetailView,self).get_context_data(*args,**kwargs)
        cart_obj,new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self,*args,**kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        try:
            instance = Shoe.objects.get(slug=slug,active=True)
        except Shoe.DoesNotExist:
            raise Http404('Not Found')
        except Shoe.MultipleObjectsReturned:
            qs = Shoe.objects.filter(slug=slug,active=True)
            instance = qs.first()
        except:
            raise Http404('object not found')
        return instance
