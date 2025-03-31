from django.shortcuts import render,redirect
from django.views.generic import TemplateView, View, CreateView, DetailView,FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from django.db.models import Sum,Count,F
from django.views.generic import TemplateView, View, CreateView, DetailView,FormView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core.paginator import Paginator
from .forms import *
from .models import *



class UserRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('myapp:UserLoginView')
        return super().dispatch(request, *args, **kwargs)


class UserLoginView(FormView):
    template_name = 'login.html'
    form_class = ULoginForm
    success_url = reverse_lazy('myapp:DashboardView')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data['password']
        usr = authenticate(username=username, password=password)

        if usr is not None:
            login(self.request, usr)

        else:
            return render(self.request, self.template_name, {'form': self.form_class, 'error': 'Invalid user login!'})
        return super().form_valid(form)

class UserLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('myapp:UserLoginView')


class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard.html')