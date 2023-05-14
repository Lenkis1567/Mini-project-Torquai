from django.urls               import reverse_lazy
from utils                     import DataMixin
from django.shortcuts          import render
from django.views.generic      import CreateView, UpdateView
from .forms                    import RegistrerUserForm
from utils                     import *
from django.contrib.auth       import logout, login
from django.shortcuts          import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

# from django.contrib.auth

# Create your views here.
class RegisterUser (DataMixin, CreateView):
    form_class = RegistrerUserForm
    template_name = 'account/registry.html'
    success_url = reverse_lazy('main_page_path')
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
        
    
class UserAuthentication(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'account/login.html'
    success_url = reverse_lazy('search_path')
    

def logout_user (request):
    logout(request)
    return redirect('main_page_path')