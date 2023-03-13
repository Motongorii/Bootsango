from django.shortcuts import render


def homepage(request):
    return render(request, 'Home.html')

def aboutuspage(request):
    return render(request, 'About us.html')

def Blogpage(request):
    return render(request, 'Blog.html')

def contactpage(request):
    return render(request, 'Contact.html')

def productpage(request):
    return render(request, 'Products.html')

def servicepage(request):
    return render(request, 'Service.html')

def indexpage(request):
    return render(request, 'Index.html')


