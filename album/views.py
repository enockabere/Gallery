from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image,Category, Location

# Create your views here.
def all_images(request):
    try:
        location = request.GET.get('location')
    except AttributeError:
        raise Http404()
        assert False
    if location == None:
        photos = Image.objects.all()
    else:
         photos = Image.location_filter(location)
    categories = Category.objects.all()
    locations = Location.objects.all()
    
    return render(request, 'all-images/all-images.html',{"categories":categories,"photos":photos,"locations":locations})

def single_image(request, pk):
    try:
        showurl=request._current_scheme_host+request.path
    except AttributeError:
        raise Http404()
        assert False
    photo = Image.objects.get(id=pk)
    return render(request, 'all-images/single-img.html',{"photo":photo,"showurl":showurl})

def search_results(request):
    if 'search' in request.GET and request.GET["search"]:
        search_query = request.GET.get("search")
        searched_images = Category.search_by_category(search_query)
        message = f"{search_query}"
        photos = Image.objects.all()
        return render(request, 'all-images/search.html',{"message":message,"images":searched_images,"photos":photos})
    else:
        message = "You haven't searched for any item"
        return render(request,"all-images/search.html",{"message":message})