from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .forms import RegistrationForm
from django.urls import reverse_lazy

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
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid information. Please try again.')
        return super().form_invalid(form)
    

class SignOut(LogoutView):
    def get_success_url(self):
        messages.success(self.request, 'Signed out successfully')
        return reverse_lazy('home')