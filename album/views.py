from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Image,Category

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
def all_images(request):
    date = dt.date.today()
    my_album = Image.nairobi_pics()
    return render(request, 'all-images/all-images.html',{"date":date,"my_album":my_album})
def single_image(request, pk):
    date = dt.date.today()
    return render(request, 'all-images/single-img.html',{"date":date,})
def search_results(request):
    if 'search' in request.GET and request.GET["search"]:
        search_query = request.GET.get("search")
        searched_images = Category.search_by_category(search_query)
        message = f"{search_query}"
        return render(request, 'all-images/search.html',{"message":message,"images":searched_images})
    else:
        message = "You haven't searched for any item"
        return render(request,"all-images/search.html",{"message":message})