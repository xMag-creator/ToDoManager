from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from works_list.models import ZeroLevel
from works_list.form import AddWorkForm


class WorksListView(ListView):
    # view all works
    model = ZeroLevel
    context_object_name = 'works'
    template_name = 'works_list_templates/works_list_view.html'


class CreateWorkView(CreateView):
    # view all works
    model = ZeroLevel
    form_class = AddWorkForm
    template_name = 'works_list_templates/add_work.html'
    success_url = reverse_lazy('works_list')


class DeleteWorkView(DeleteView):
    # view to confirm delete project
    model = ZeroLevel
    template_name = 'works_list_templates/delete_work.html'
    success_url = reverse_lazy('works_list')


class EditWorkView(UpdateView):
    model = ZeroLevel
    form_class = AddWorkForm
    context_object_name = 'work'
    template_name = 'works_list_templates/edit_work.html'
    success_url = reverse_lazy('works_list')
