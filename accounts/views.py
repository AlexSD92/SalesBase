from django.views.generic import ListView
from .models import AccountsModel


class AccountsListView(ListView):
    model = AccountsModel
    template_name="accounts/accounts_list.html"
    # context = {'accounts': AccountsModel.objects.all()}




