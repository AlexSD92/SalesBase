from django.views.generic import ListView, DetailView
from .models import AccountsModel


class AccountsListView(ListView):
    model = AccountsModel
    template_name='accounts/accounts_list.html'

    def get_queryset(self):
        return AccountsModel.objects.filter(owner = self.request.user)
        

class AccountsDetailView(DetailView):
    model = AccountsModel
    template_name='accounts/accounts_detail.html'

    def get_queryset(self):
        return AccountsModel.objects.filter(owner = self.request.user)


class DashboardAccountsListView(ListView):
    model = AccountsModel
    template_name='dashboard.html'

    def get_queryset(self):
        return AccountsModel.objects.filter(owner = self.request.user)