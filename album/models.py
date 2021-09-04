from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email=models.EmailField()
    
    def __str__(self):
        return self.first_name
    def save_user(self):
        self.save()
class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
class Location(models.Model):
    place = models.CharField(max_length=100)
class Image(models.Model):
    image_name = models.CharField(max_length=100)
    image_description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    places = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    post_date = models.DateTimeField(auto_now_add=True)
