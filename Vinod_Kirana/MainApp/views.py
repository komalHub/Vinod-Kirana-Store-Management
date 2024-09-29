from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Homepage.html')

def about(request):
    return render(request, 'About.html')

def prducts(request):
    return render(request, 'Products.html')

def contact(request):
    return render(request, 'Contact.html')