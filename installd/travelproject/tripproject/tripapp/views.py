from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    object=Team.objects.all()


    return render(request,"index.html",{'result':obj, 'run':object})
#def addition(request):
 #   x=int(request.GET['num1'])
  #  y=int(request.GET['num2'])
   # res=x+y
   # return render(request,"about.html",{'result':res})
