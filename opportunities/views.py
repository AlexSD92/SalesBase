from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import OpportunitiesModel


class OpportunitiesListView(ListView):
    model = OpportunitiesModel
    template_name='opportunities/opportunities_list.html'

    def get_queryset(self):
        return OpportunitiesModel.objects.filter(owner = self.request.user)
        

class OpportunitiesDetailView(DetailView):
    model = OpportunitiesModel
    template_name='opportunities/opportunities_detail.html'

    def get_queryset(self):
        return OpportunitiesModel.objects.filter(owner = self.request.user)


class CreateOpportunitiesView(CreateView):
    model = OpportunitiesModel
    template_name = 'opportunities/opportunities_create.html'
    fields = ['opportunity_name', 'account_name', 'opportunity_value']
    success_url = reverse_lazy('opportunities-list-view')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class UpdateOpportunitiesView(UpdateView):
    model = OpportunitiesModel
    template_name = 'opportunities/opportunities_update.html'
    fields = ['opportunity_name', 'account_name', 'opportunity_value']
    success_url = reverse_lazy('opportunities-list-view')


class DeleteOpportunitiesView(DeleteView):
    model = OpportunitiesModel
    template_name = 'opportunities/opportunities_delete.html'
    success_url = reverse_lazy('opportunities-list-view')