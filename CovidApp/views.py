from django.shortcuts import render, HttpResponse
from .models import Contact

def index(request):
    return render(request,'home.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        tell=request.POST.get('tell','')
        #print(name,email,phone,tell)
        contact=Contact(name=name,email=email,phone=phone,tell=tell)
        contact.save()

    return render(request,'contact.html')
def hospital(request):
    return HttpResponse("THIS IS HOSPITAL PAGE")
def ecmo(request):
    return HttpResponse("THIS IS ecmo PAGE")


# Create your views here.
