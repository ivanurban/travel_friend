from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import register

from .forms import UserRegistrationForm

from django.contrib.auth import get_user_model

# Create your tests here.

class LoginpageTests(SimpleTestCase):

    def test_loginpage_status_code(self):
        response = self.client.get('/useraccount')
        self.assertEqual(response.status_code, 301)

class RegisterPageTests(TestCase):
    
    def setUp(self):
        url=reverse('useraccount:register')
        self.response = self.client.get(url)

    def test_register_template(self):
        self.assertEqual(self.response.status_code,200)
        self.assertTemplateUsed(self.response, 'useraccount/register.html')
        self.assertContains(self.response, 'Create an account')
        self.assertContains(self.response, 'Repeat password:')
        self.assertNotContains(self.response, 'lalalalalalalalalal bja.')


    def test_register_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form , UserRegistrationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_register_view(self):
        view = resolve('/useraccount/register/')
        self.assertEqual(view.func.__name__, register.__name__)
    
class RegisterUserTests(TestCase):

    username='tester'
    #first_name='john'
    email='newuser@email.com'

    def setUp(self):
        url=reverse('useraccount:register')
        self.response = self.client.get(url)

    def test_register_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'useraccount/register.html')
        self.assertContains(self.response, 'Create an account')
        self.assertContains(self.response, 'Repeat password:')
        self.assertNotContains(self.response, 'lalalalalalalalalal bja.')

    def test_register_form(self):
        new_user = get_user_model().objects.create_user(self.username,  self.email)

        
        self.assertEqual(get_user_model().objects.all().count(), 1)

        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        #self.assertEqual(get_user_model().objects.all()[0].first_name, self.first_name)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)






    
