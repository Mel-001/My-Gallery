# from django.conf.urls import url
from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns=[
    # url(r'^$',views.pics,name='pics'),
    # url(r'^single_pic/(\d+)',views.single_pic),
    # url(r'^search/',views.search_results),
    # url(r'^location/(\d+)',views.viewPics_by_location),
    # url(r'^category/(\d+)',views.viewPics_by_category),
    path('admin/', admin.site.urls),
    path('', views.pics, name='pics'),
    path('single_pic/', views.single_pic),
    path('search/', views.search_results),
    path('location/', views.viewPics_by_location),
    path('category/', views.viewPics_by_category),
    ]



if settings.DEBUG: 
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)