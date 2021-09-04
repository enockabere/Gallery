from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
def all_images(request):
    date = dt.date.today()
    return render(request, 'all-images/all-images.html',{"date":date,})
def single_image(request):
    date = dt.date.today()
    return render(request, 'all-images/single-img.html',{"date":date,})