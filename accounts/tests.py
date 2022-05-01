from django.test import TestCase
from django.urls import reverse

from users.models import CustomUserModel
from .models import AccountsModel


class AccountsModelTests(TestCase):

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

    def test_is_the_url_at_the_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_is_the_url_available_by_name(self):
        response = self.client.get(reverse('account-list-view'))
        self.assertEqual(response.status_code, 200)

    def test_is_the_template_name_correct(self):
        response = self.client.get(reverse('account-list-view'))
        self.assertTemplateUsed(response, 'accounts/accounts_list.html')
