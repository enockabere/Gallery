from django.contrib import admin
from . models import User, Image, Location, Category

# Register your models here.
admin.site.register(User)
admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)
