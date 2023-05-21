from django.shortcuts import render, HttpResponse 

# Create your views here.
def index(request):
    return render(request, 'index.html')

def linear_regression(request):
    return render(request, 'linear_regression.html')

def image_class(request):
    return render(request, 'image_class.html')