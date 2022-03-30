from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import User,Image,Category,Location
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

