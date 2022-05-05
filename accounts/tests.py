from django.test import TestCase
from django.urls import reverse

from users.models import CustomUserModel
from django.contrib.auth import get_user_model
from .models import AccountsModel

class AccountsModelTestsUnauth(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.account = AccountsModel.objects.create(
            account_name='Test', account_ind='Testing', account_size='1', account_rev='1', owner=CustomUserModel.objects.create(username='testuser'))

    def test_AccountsModel_data(self):
        self.assertEqual(self.account.account_name, 'Test')
        self.assertEqual(self.account.account_ind, 'Testing')
        self.assertEqual(self.account.account_size, '1')
        self.assertEqual(self.account.account_rev, '1')
        self.assertEqual(self.account.owner, CustomUserModel.objects.get(id=1))

    def test_URL_correct_location_accounts_list(self):
        response = self.client.get('/accounts/')
        self.assertEqual(response.status_code, 302)

    def test_URL_available_by_name_accounts_list(self):
        response = self.client.get(reverse('account-list-view'))
        self.assertEqual(response.status_code, 302)

    def test_URL_correct_location_accounts_detail(self):
        response = self.client.get('/accounts/1/')
        self.assertEqual(response.status_code, 302)

    def test_URL_correct_location_accounts_detail(self):
        response = self.client.get('/accounts/create/')
        self.assertEqual(response.status_code, 302)

    def test_URL_correct_location_accounts_update(self):
        response = self.client.get('/accounts/1/update/')
        self.assertEqual(response.status_code, 302)

    def test_URL_correct_location_ccounts_delete(self):
        response = self.client.get('/accounts/1/delete/')
        self.assertEqual(response.status_code, 302)

    # def test_AccountsListView(self):
    #     response = self.client.get(reverse('account-list-view'))
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTemplateUsed(response, 'accounts/accounts_list.html')