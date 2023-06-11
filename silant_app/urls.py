from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('car/', CarList.as_view(), name='table_car'),
    path('service/', ServiceList.as_view(), name='table_service'),
    path('claims/', ClaimsList.as_view(), name='table_claims'),
    path('car/<slug:car_slug>/', ShowCar.as_view(), name='car'),
    path('service/<slug:service_slug>/', ShowService.as_view(), name='service'),
    path('claims/<slug:claims_slug>/', ShowClaims.as_view(), name='claims'),
    path('search/', SearchResults.as_view(), name='search_results'),
    path('add_car/', AddCar.as_view(), name='add_car'),
    path('add_service/', AddService.as_view(), name='add_service'),
    path('add_claims/', AddClaims.as_view(), name='add_claims'),
]