from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model
from .models import OpportunitiesModel
from djmoney.models.fields import Money

class OpportunitiesModelTestsUnauth(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='testuser', password='AVeryComplicatedPassword1')
        cls.opportunity = OpportunitiesModel.objects.create(opportunity_name='Test', opportunity_value='1', owner=cls.user)

    def test_OpportunitiesModel_data(self):
        self.assertEqual(self.opportunity.opportunity_name, 'Test')
        self.assertEqual(self.opportunity.opportunity_value, Money('1', 'GBP'))
        self.assertEqual(self.opportunity.owner.username, 'testuser')

# USER AUTHENTICATED TESTS

    def test_authenticated_URL_correct_location_opportunities_list(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.get('/opportunities/')
        self.assertEqual(response.status_code, 200) 

    def test_authenticated_URL_available_by_name_opportunities_list(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.get(reverse('opportunities-list-view'))
        self.assertEqual(response.status_code, 200)

    def test_authenticated_URL_correct_location_opportunities_detail(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.get('/opportunities/1-Test')
        self.assertEqual(response.status_code, 200)

    def test_authenticated_URL_correct_location_opportunities_create(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.get('/opportunities/create/')
        self.assertEqual(response.status_code, 200)

    def test_authenticated_URL_available_by_name_create_opportunity(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.get(reverse('create-opportunity'))
        self.assertEqual(response.status_code, 200)

    def test_authenticated_URL_correct_location_opportunities_update(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.get('/opportunities/1/update/')
        self.assertEqual(response.status_code, 200)

    def test_authenticated_URL_correct_location_opportunities_delete(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.get('/opportunities/1/delete/')
        self.assertEqual(response.status_code, 200)

# USER UNAUTHENTICATED TESTS

    def test_URL_correct_location_opportunities_list(self):
        response = self.client.get('/opportunities/')
        self.assertEqual(response.status_code, 302) 

    def test_URL_available_by_name_opportunities_list(self):
        response = self.client.get(reverse('opportunities-list-view'))
        self.assertEqual(response.status_code, 302)

    def test_URL_correct_location_opportunities_detail(self):
        response = self.client.get('/opportunities/1-Test')
        self.assertEqual(response.status_code, 302)

    def test_URL_correct_location_opportunities_create(self):
        response = self.client.get('/opportunities/create/')
        self.assertEqual(response.status_code, 302)

    def test_URL_available_by_name_create_opportunity(self):
        response = self.client.get(reverse('create-opportunity'))
        self.assertEqual(response.status_code, 302)

    def test_URL_correct_location_opportunities_update(self):
        response = self.client.get('/opportunities/1/update/')
        self.assertEqual(response.status_code, 302)

    def test_URL_correct_location_opportunities_delete(self):
        response = self.client.get('/opportunities/1/delete/')
        self.assertEqual(response.status_code, 302)

# FORM TESTS

    def test_create_opportunity_form(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.post(
            reverse('create-opportunity'),
            {
                'opportunity_name':'Test',
                'opportunity_value':'1',
                'owner':self.user,
            },)
        self.assertEqual(self.opportunity.opportunity_name, 'Test')
        self.assertEqual(self.opportunity.opportunity_value, Money('1', 'GBP'))
        self.assertEqual(self.opportunity.owner.username, 'testuser')

    def test_delete_opportunity(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.post(reverse('delete-opportunity', args='1'))
        self.assertEqual(response.status_code, 302)