from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import AccountsModel
from contacts.models import ContactsModel
from opportunities.models import OpportunitiesModel


class AccountsListView(ListView):
    model = AccountsModel
    template_name='accounts/accounts_list.html'

    def get_queryset(self):
        return AccountsModel.objects.filter(owner = self.request.user)
        

class AccountsDetailView(DetailView):
    model = AccountsModel
    template_name='accounts/accounts_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AccountsDetailView, self).get_context_data(**kwargs)
        # context['contactsmodel'] = ContactsModel.objects.filter(contact_company = self.request.account_name.id)
        context['opportunitiesmodel'] = OpportunitiesModel.objects.filter(owner = self.request.user)
        return context


class DashboardListView(ListView):
    model = AccountsModel
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardListView, self).get_context_data(**kwargs)
        context['contactsmodel'] = ContactsModel.objects.filter(owner = self.request.user)
        context['opportunitiesmodel'] = OpportunitiesModel.objects.filter(owner = self.request.user)
        return context

    def get_queryset(self):
        return AccountsModel.objects.filter(owner = self.request.user)


class CreateAccountsView(SuccessMessageMixin, CreateView):
    model = AccountsModel
    template_name = 'accounts/accounts_create.html'
    fields = ['account_name', 'account_ind', 'account_size']
    success_url = reverse_lazy('account-list-view')
    success_message = 'Account for %(account_name)s successfully created!'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class UpdateAccountsView(SuccessMessageMixin, UpdateView):
    model = AccountsModel
    template_name = 'accounts/accounts_update.html'
    fields = ['account_name', 'account_ind', 'account_size']
    success_url = reverse_lazy('account-list-view')
    success_message = '%(account_name)s successfully updated!'


class DeleteAccountsView(SuccessMessageMixin, DeleteView):
    model = AccountsModel
    template_name = 'accounts/accounts_delete.html'
    success_url = reverse_lazy('account-list-view')
    success_message = 'Account successfully deleted!'