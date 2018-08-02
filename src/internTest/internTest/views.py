from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context={'title':'MyInternTest'}

    return render(request,'views/home-page.html',context)