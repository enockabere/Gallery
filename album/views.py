from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Image,Category

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
def all_images(request):

    categories = Category.objects.all()
    photos = Image.objects.all()
    return render(request, 'all-images/all-images.html',{"categories":categories,"photos":photos})

def single_image(request, pk):
    
    photo = Image.objects.get(id=pk)
    return render(request, 'all-images/single-img.html',{"photo":photo})

def search_results(request):
    if 'search' in request.GET and request.GET["search"]:
        search_query = request.GET.get("search")
        searched_images = Category.search_by_category(search_query)
        message = f"{search_query}"
        return render(request, 'all-images/search.html',{"message":message,"images":searched_images})
    else:
        message = "You haven't searched for any item"
        return render(request,"all-images/search.html",{"message":message})