from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ContactsModel


class ContactsListView(ListView):
    model = ContactsModel
    template_name='contacts/contacts_list.html'
    paginate_by = 5

    def get_queryset(self):
        return ContactsModel.objects.filter(owner = self.request.user).order_by('id')
        

class ContactsDetailView(DetailView):
    model = ContactsModel
    template_name='contacts/contacts_detail.html'
    query_pk_and_slug: True

    def get_queryset(self):
        return ContactsModel.objects.filter(owner = self.request.user)


class CreateContactsView(SuccessMessageMixin, CreateView):
    model = ContactsModel
    template_name = 'contacts/contacts_create.html'
    fields = ['contact_name', 'contact_role']
    success_url = reverse_lazy('contacts-list-view')
    success_message = 'Contact, %(contact_name)s, successfully created!'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class UpdateContactsView(SuccessMessageMixin, UpdateView):
    model = ContactsModel
    template_name = 'contacts/contacts_update.html'
    fields = ['contact_name', 'contact_role']
    success_url = reverse_lazy('contacts-list-view')
    success_message = '%(contact_name)s successfully updated!'


class DeleteContactsView(SuccessMessageMixin, DeleteView):
    model = ContactsModel
    template_name = 'contacts/contacts_delete.html'
    success_url = reverse_lazy('contacts-list-view')
    success_message = 'Contact successfully updated!'