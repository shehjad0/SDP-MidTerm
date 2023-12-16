from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView
from .models import CarModel, CommentModel, OrderModel
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
        template_name = 'car/details.html'
        context_object_name = 'car'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            car = self.get_object()
            context["car"] = car
            context['comments'] = CommentModel.objects.filter(car_model=self.object).order_by('-created_on')
            context['comment_form'] = CommentForm()
            return context

        def post(self, request, *args, **kwargs):
            self.object = self.get_object()
            context = self.get_context_data()

            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.car_model = self.object
                new_comment.save()
                comment_form = CommentForm()

            context['comment_form'] = comment_form
            return self.render_to_response(context)
    
    
@login_required
def buy(request, car_id):
    car_model = CarModel.objects.get(pk=car_id)

    if car_model.quantity > 0:
        order = OrderModel(user=request.user, car_model=car_model, quantity=1, total_price=car_model.price)
        order.save()
        car_model.quantity -= 1
        car_model.save()

    return redirect('order_history')

@login_required
def order_history(request):
    orders = OrderModel.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'car/order_history.html', {'orders': orders})