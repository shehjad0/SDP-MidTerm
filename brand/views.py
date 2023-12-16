from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView
from .models import BrandModel
from .forms import BrandForm

@method_decorator(login_required, name='dispatch')
class AddBrandView(CreateView):
    model = BrandModel
    template_name = 'brand/index.html'
    form_class = BrandForm
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class EditBrandView(UpdateView):
    model = BrandModel
    template_name = 'brand/index.html'
    form_class = BrandForm
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class DeleteBrandView(View):
    def get(self, request, pk):
        brand = BrandModel.objects.get(pk=pk)
        brand.delete()
        return redirect('home')