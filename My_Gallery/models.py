from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=300, blank=True)


    def __str__(self):
        return self.first_name

class Image(models.Model):
    image = models.ImageField(upload_to= 'pictures/')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    location = models.ForeignKey('Location',on_delete = models.CASCADE,default=None)
    category = models.ForeignKey('Category', on_delete = models.CASCADE,default=None)
    author = models.ForeignKey(User,on_delete = models.CASCADE)


    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()

    
    @classmethod
    def all_images(cls):
        pics = cls.objects.all()
        return pics

    @classmethod
    def get_one_image(cls,id):
        pictures = cls.objects.filter(id = id)
        return pictures

    @classmethod
    def search_by_name(cls,search_term):
        image = cls.objects.filter(name__icontains=search_term)
        return image

    
    @classmethod
    def view_pictures_by_location(cls,location):
        location_pics = cls.objects.filter(location= location)

        return location_pics

    @classmethod
    def view_pictures_by_category(cls,category):
        category = cls.objects.filter(category = category)
        return category 


class Category(models.Model):
    category_name = models.CharField(max_length=80)


    def save_category(self):
        self.save()
        
    @classmethod
    def get_categories(cls):
        categories = cls.objects.all()

        return categories

    def __str__(self):
        return self.category_name 
    
class Location(models.Model):
    location_name = models.CharField(max_length=80)
    def save_location(self):
        self.save()

    def __str__(self):
        return self.location_name 

    @classmethod
    def get_location(cls):
        locations = cls.objects.all()
        return locations


