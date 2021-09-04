from django.contrib import admin
from . models import User, Image, Location, Category

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)
# Register your models here.
admin.site.register(User)
admin.site.register(Image,ImageAdmin)
admin.site.register(Location)
admin.site.register(Category)
