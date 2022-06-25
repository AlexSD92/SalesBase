from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model
from .models import ContactsModel

class ContactsModelTestsUnauth(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='testuser', password='AVeryComplicatedPassword1')
        cls.contact = ContactsModel.objects.create(contact_name='Test', contact_role='1', owner=cls.user)

    def test_ContactsModel_data(self):
        self.assertEqual(self.contact.contact_name, 'Test')
        self.assertEqual(self.contact.contact_role, '1')
        self.assertEqual(self.contact.owner.username, 'testuser')

# USER AUTHENTICATED TESTS

    def test_authenticated_URL_correct_location_contacts_list(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 200) 

    def test_authenticated_URL_available_by_name_contacts_list(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.get(reverse('contacts-list-view'))
        self.assertEqual(response.status_code, 200)

    def test_authenticated_URL_correct_location_contacts_detail(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.get('/contacts/1-Test')
        self.assertEqual(response.status_code, 200)

    def test_authenticated_URL_correct_location_contacts_create(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.get('/contacts/create/')
        self.assertEqual(response.status_code, 200)

    def test_authenticated_URL_available_by_name_create_contact(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.get(reverse('create-contact'))
        self.assertEqual(response.status_code, 200)

    def test_authenticated_URL_correct_location_contacts_update(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.get('/contacts/1/update/')
        self.assertEqual(response.status_code, 200)

    def test_authenticated_URL_correct_location_contacts_delete(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.get('/contacts/1/delete/')
        self.assertEqual(response.status_code, 200)

# USER UNAUTHENTICATED TESTS

    def test_URL_correct_location_contacts_list(self):
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 302) 

    def test_URL_available_by_name_contacts_list(self):
        response = self.client.get(reverse('contacts-list-view'))
        self.assertEqual(response.status_code, 302)

    def test_URL_correct_location_contacts_detail(self):
        response = self.client.get('/contacts/1-Test')
        self.assertEqual(response.status_code, 302)

    def test_URL_correct_location_contacts_create(self):
        response = self.client.get('/contacts/create/')
        self.assertEqual(response.status_code, 302)

    def test_URL_available_by_name_create_contact(self):
        response = self.client.get(reverse('create-contact'))
        self.assertEqual(response.status_code, 302)

    def test_URL_correct_location_contacts_update(self):
        response = self.client.get('/contacts/1/update/')
        self.assertEqual(response.status_code, 302)

    def test_URL_correct_location_contacts_delete(self):
        response = self.client.get('/contacts/1/delete/')
        self.assertEqual(response.status_code, 302)

# FORM TESTS

    def test_create_contact_form(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.post(
            reverse('create-contact'),
            {
                'contact_name':'Test',
                'contact_role':'1',
                'owner':self.user,
            },)
        self.assertEqual(self.contact.contact_name, 'Test')
        self.assertEqual(self.contact.contact_role, '1')
        self.assertEqual(self.contact.owner.username, 'testuser')

    def test_update_contact_form(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.post(
            reverse('update-contact', args='1'),
            {
                'contact_name':'Testing',
                'contact_role':'2',  
            },)

        self.assertEqual(ContactsModel.objects.last().contact_name, 'Testing')
        self.assertEqual(ContactsModel.objects.last().contact_role, '2')

    def test_delete_contact(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.post(reverse('delete-contact', args='1'))
        self.assertEqual(response.status_code, 302)