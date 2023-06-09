from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    item= Product.objects.all()
    return render(request,'home.html',{'item':item}) 

def about(request):
    return render(request,'about.html') 

def contact(request):
    details= Contact.objects.all()
    return render(request,'contact.html',{'details': details}) 

def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if Contact.objects.filter(email = email).exists():
            messages.error(request,'Email is already exists')
            return redirect('/contact/')
        else:
            Contact.objects.create(name = name, email = email, subject = subject,
                                   message = message)
            messages.success(request,'Details successfully added')
            details = Contact.objects.all()
            return render(request,'contact.html',{'details':details})