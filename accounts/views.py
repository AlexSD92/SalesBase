from django.views.generic import ListView, DetailView, TemplateView
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

    def get_queryset(self):
        return AccountsModel.objects.filter(owner = self.request.user)


class DashboardListView(ListView):
    model = AccountsModel
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardListView, self).get_context_data(**kwargs)
        context['contactsmodel'] = ContactsModel.objects.all()
        context['opportunitiesmodel'] = OpportunitiesModel.objects.all()
        return context


class CreateAccountsView(CreateView):
    model = AccountsModel
    template_name = 'accounts/accounts_create.html'
    fields = ['account_name', 'account_ind', 'account_size']
    success_url = reverse_lazy('account-list-view')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class UpdateAccountsView(UpdateView):
    model = AccountsModel
    template_name = 'accounts/accounts_update.html'
    fields = ['account_name', 'account_ind', 'account_size']
    success_url = reverse_lazy('account-list-view')


class DeleteAccountsView(DeleteView):
    model = AccountsModel
    template_name = 'accounts/accounts_delete.html'
    success_url = reverse_lazy('account-list-view')