from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from django.db.models import Q
from .forms import *
from .models import *



def index(request):
    return render(request, 'silant_app/index.html')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'silant_app/login.html'

    def get_success_url(self):
        return reverse_lazy('table_car')


class CarList(ListView):
    model = Car
    template_name = 'silant_app/table_car.html'
    context_object_name = 'posts'


class ServiceList(ListView):
    model = Service
    template_name = 'silant_app/table_service.html'
    context_object_name = 'posts'


class ClaimsList(ListView):
    model = Claims
    template_name = 'silant_app/table_claims.html'
    context_object_name = 'posts'


class ShowCar(DetailView):
    model = Car
    template_name = 'silant_app/detail_car.html'
    slug_url_kwarg = 'car_slug'
    context_object_name = 'car'


class ShowService(DetailView):
    model = Service
    template_name = 'silant_app/detail_service.html'
    slug_url_kwarg = 'service_slug'
    context_object_name = 'service'


class ShowClaims(DetailView):
    model = Claims
    template_name = 'silant_app/detail_claims.html'
    slug_url_kwarg = 'claims_slug'
    context_object_name = 'claims'


class SearchResults(ListView):
    model = Car
    template_name = 'silant_app/search_results.html'
 
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Car.objects.filter(
            Q(machine_serial_number__icontains=query)
        )
        return object_list


class AddCar(CreateView):
    form_class=AddCarForm
    template_name='silant_app/add_car.html'


class AddService(CreateView):
    form_class=AddServiceForm
    template_name='silant_app/add_service.html'


class AddClaims(CreateView):
    form_class=AddClaimsForm
    template_name='silant_app/add_claims.html'
