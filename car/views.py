from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView
from .models import CarModel
from .forms import CarForm, CommentForm

@method_decorator(login_required, name='dispatch')
class AddCarView(CreateView):
    model = CarModel
    template_name = 'car/index.html'
    form_class = CarForm
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class EditCarView(UpdateView):
    model = CarModel
    template_name = 'car/index.html'
    form_class = CarForm
    success_url = reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class DeleteCarView(View):
    def get(self, request, pk):
        car = CarModel.objects.get(pk=pk)
        car.delete()
        return redirect('home')
    
class CarDetails(DetailView):
    model = CarModel
    pk_url_kwarg = 'pk'
    template_name = "car/details.html"
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.get_object()
        comments = car.comments.all()
        comment_form = CommentForm()
        
        context["car"] = car
        context["comments"] = comments
        context["comment_form"] = comment_form
        
        return context
    
    
def buy(request, pk=None):
    if pk is not None:
        car = get_object_or_404(CarModel, pk=pk)
        car.quantity -= 1
        car.save()
        return redirect("home")
