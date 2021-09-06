from django.shortcuts import render
from django.http import HttpResponse,Http404
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
    
    showurl=request._current_scheme_host+request.path
    
    photo = Image.objects.get(id=pk)
    return render(request, 'all-images/single-img.html',{"photo":photo,"showurl":showurl})

def search_results(request):
    if 'search' in request.GET and request.GET["search"]:
        search_query = request.GET.get("search")
        searched_images = None
        searched_category = Category.search_by_category(search_query)
        for item in searched_category:
            searched_images = Image.search_by_category(item.id)
        message = f"{search_query}"
        showurl=request._current_scheme_host+request.path
        
        return render(request, 'all-images/search.html',{"message":message,"showurl":showurl,"images":searched_images})
    else:
        message = "You haven't searched for any item"
        return render(request,"all-images/search.html",{"message":message})
