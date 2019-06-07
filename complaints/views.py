from django.shortcuts import render
from .forms import ComplaintAddForm
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Complaint


class ComplaintAddView(CreateView):
    template_name = "complaints/add.html"
    form_class = ComplaintAddForm
    model = Complaint


class ComplaintUpdateView(CreateView):
    template_name = "complaints/update.html"
    form_class = ComplaintAddForm
    model = Complaint


class ComplaintDeleteView(CreateView):
    template_name = "complaints/delete.html"
    form_class = ComplaintAddForm
    model = Complaint
