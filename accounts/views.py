from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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
    template_name = 'dashboard.html'

    def get_queryset(self):
        return AccountsModel.objects.filter(owner = self.request.user)


class CreateAccountsView(CreateView):
    model = AccountsModel
    template_name = 'accounts/accounts_create.html'
    fields = ['account_name', 'account_ind', 'account_size', 'account_rev', 'owner']
    success_url = reverse_lazy('account-list-view')


class UpdateAccountsView(UpdateView):
    model = AccountsModel
    template_name = 'accounts/accounts_update.html'
    fields = ['account_name', 'account_ind', 'account_size', 'account_rev']
    success_url = reverse_lazy('account-list-view')


class DeleteAccountsView(DeleteView):
    model = AccountsModel
    template_name = 'accounts/accounts_delete.html'
    success_url = reverse_lazy('account-list-view')