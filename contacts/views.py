from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ContactsModel


class ContactsListView(ListView):
    model = ContactsModel
    template_name='contacts/contacts_list.html'

    def get_queryset(self):
        return ContactsModel.objects.filter(owner = self.request.user)
        

class ContactsDetailView(DetailView):
    model = ContactsModel
    template_name='contacts/contacts_detail.html'

    def get_queryset(self):
        return ContactsModel.objects.filter(owner = self.request.user)


class DashboardContactsListView(ListView):
    model = ContactsModel
    template_name = 'dashboard.html'

    def get_queryset(self):
        return ContactsModel.objects.filter(owner = self.request.user)


class CreateContactsView(CreateView):
    model = ContactsModel
    template_name = 'contacts/contacts_create.html'
    fields = ['contact_name', 'contact_company', 'contact_role', 'contact_opp', 'owner']
    success_url = reverse_lazy('contacts-list-view')


class UpdateContactsView(UpdateView):
    model = ContactsModel
    template_name = 'contacts/contacts_update.html'
    fields = ['contact_name', 'contact_company', 'contact_role', 'contact_opp']
    success_url = reverse_lazy('contacts-list-view')


class DeleteContactsView(DeleteView):
    model = ContactsModel
    template_name = 'contacts/contacts_delete.html'
    success_url = reverse_lazy('contacts-list-view')