from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .forms import RegistrationForm, ProfileUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User

class SignUp(View):
    template_name = 'account/signup.html'
    form_class = RegistrationForm
    
    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. Please sign in.')
            return redirect('sign_in')
        return render(request, self.template_name, {'form': form})


class SignIn(LoginView):
    template_name = 'account/signin.html'
    
    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Signed in successfully')
        return super().form_valid(form)
    

class SignOut(LogoutView):
    def get_success_url(self):
        messages.success(self.request, 'Signed out successfully')
        return reverse_lazy('home')
    

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    template_name = 'account/profile.html'

    def get(self, request):
        user = request.user
        return render(request, self.template_name, {'user': user})
    
    
@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = 'account/profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Profile update failed. Please try again.')
        return super().form_invalid(form)