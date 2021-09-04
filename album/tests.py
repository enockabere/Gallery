from django.test import TestCase
from  .models import User,Category,Location,Image

# Create your tests here.
class UserTestCase(TestCase):
    
    #setup method
    def setUp(self):
        self.enock = User(first_name='Enock',last_name='Abere', email = 'enockabere@gmail.com')
    #testing instance
    def test_user_instance(self):
        self.assertTrue(isinstance(self.enock, User))
    #testing save method
    def test_user_save(self):
        self.enock.save_user()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)
class ImageTest(TestCase):
    
    def setUp(self):
        self.enock = User(first_name='Enock',last_name='Abere', email = 'enockabere@gmail.com')
        self.enock.save_user()
           
        #creating a new category and saving it
        self.new_category = Category(name='Horror')
        self.new_category.save()

        #creating new location and save it
        self.new_location = Location(places='Nairobi')
        self.new_location.save()
        
        self.new_image = Image(image_name="Personal", image_description="Nobody Sleeps in the Woods Tonight",user=self.enock)
        self.new_image.save()
        
        self.new_image.category.add(self.new_category)
        self.new_image.places.add(self.new_location)
        
    def tearDown(self):
        User.objects.all().delete()
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()
