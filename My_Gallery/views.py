from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import User,Image,Category,Location
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def pics(request):
    category = Category.get_categories()
    pictures = Image.all_images ()
    location_pics = Location.get_location()

    return render(request,'pictures.html',{'pictures': pictures, 'category': category, 'location_pics':location_pics })

    def single_pic(request,id):
    try:
        image = Image.objects.get(id = id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"single_image.html", {"image":image})