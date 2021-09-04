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
