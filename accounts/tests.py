from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model
from .models import AccountsModel

class AccountsModelTestsUnauth(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='testuser', password='AVeryComplicatedPassword1')
        cls.account = AccountsModel.objects.create(account_name='Test', account_size='1', owner=cls.user)

    def test_AccountsModel_data(self):
        self.assertEqual(self.account.account_name, 'Test')
        self.assertEqual(self.account.account_size, '1')
        self.assertEqual(self.account.owner.username, 'testuser')

# USER AUTHENTICATED TESTS

    def test_authenticated_URL_correct_location_accounts_list(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.get('/accounts/')
        self.assertEqual(response.status_code, 200) 

    def test_authenticated_URL_available_by_name_accounts_list(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.get(reverse('account-list-view'))
        self.assertEqual(response.status_code, 200)

    def test_authenticated_URL_correct_location_accounts_detail(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.get('/accounts/1-Test')
        self.assertEqual(response.status_code, 200)

    def test_authenticated_URL_correct_location_accounts_create(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.get('/accounts/create/')
        self.assertEqual(response.status_code, 200)

    def test_authenticated_URL_available_by_name_create_account(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.get(reverse('create-account'))
        self.assertEqual(response.status_code, 200)

    def test_authenticated_URL_correct_location_accounts_update(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.get('/accounts/1/update/')
        self.assertEqual(response.status_code, 200)

    def test_authenticated_URL_correct_location_accounts_delete(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.get('/accounts/1/delete/')
        self.assertEqual(response.status_code, 200)

# USER UNAUTHENTICATED TESTS

    def test_URL_correct_location_accounts_list(self):
        response = self.client.get('/accounts/')
        self.assertEqual(response.status_code, 302) 

    def test_URL_available_by_name_accounts_list(self):
        response = self.client.get(reverse('account-list-view'))
        self.assertEqual(response.status_code, 302)

    def test_URL_correct_location_accounts_detail(self):
        response = self.client.get('/accounts/1-Test')
        self.assertEqual(response.status_code, 302)

    def test_URL_correct_location_accounts_create(self):
        response = self.client.get('/accounts/create/')
        self.assertEqual(response.status_code, 302)

    def test_URL_available_by_name_create_account(self):
        response = self.client.get(reverse('create-account'))
        self.assertEqual(response.status_code, 302)

    def test_URL_correct_location_accounts_update(self):
        response = self.client.get('/accounts/1/update/')
        self.assertEqual(response.status_code, 302)

    def test_URL_correct_location_accounts_delete(self):
        response = self.client.get('/accounts/1/delete/')
        self.assertEqual(response.status_code, 302)

# FORM TESTS

    def test_create_account_form(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.post(
            reverse('create-account'),
            {
                'account_name':'Test',
                'account_size':'1',
                'owner':self.user,
            },)
        self.assertEqual(self.account.account_name, 'Test')
        self.assertEqual(self.account.account_size, '1')
        self.assertEqual(self.account.owner.username, 'testuser')

    def test_update_account_form(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.post(
            reverse('update-account', args='1'),
            {
                'account_name':'Testing',
                'account_size':'2',  
            },)

        self.assertEqual(AccountsModel.objects.last().account_name, 'Testing')
        self.assertEqual(AccountsModel.objects.last().account_size, 2)

    def test_delete_account(self):
        self.client.login(username='testuser', password='AVeryComplicatedPassword1')
        response = self.client.post(reverse('delete-account', args='1'))
        self.assertEqual(response.status_code, 302)