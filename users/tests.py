from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

class RegisterPageTests(TestCase):

    def test_register_url_exists_at_correct_location_registeruserview(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_register_user_view_name(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_register_user_form(self):
        response = self.client.post(reverse('register'),
            {
                'username':'testuser',
                'password1':'AVeryComplicatedPswd123',
                'password2':'AVeryComplicatedPswd123',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, 'testuser')