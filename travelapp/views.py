from django.shortcuts import render,redirect
from . models import place
from . models import testmonials

# Create your views here.
def home(request):
    object1=place.objects.all()
    test=testmonials.objects.all()

    return render(request,'index.html',{'object':object1,'test':test})

def contact(request):
    return render(request,'contact.html')
    

