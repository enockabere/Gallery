from django.test import TestCase
from  .models import Category,Location,Image


class ImageTest(TestCase):
    
    def setUp(self):
         
        #creating a new category and saving it
        self.new_category = Category(name='Horror')
        self.new_category.save()

        #creating new location and save it
        self.new_location = Location(location='Nairobi')
        self.new_location.save()
        
        self.new_image = Image(name="Personal", description="Nobody Sleeps in the Woods Tonight",image = 'static/images/contact-us-1426589_640.png')
        self.new_image.save()
        
        self.new_image.category.add(self.new_category)
        self.new_image.location.add(self.new_location)
        
    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()
