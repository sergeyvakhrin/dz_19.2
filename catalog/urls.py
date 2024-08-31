from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import product_list, contact_list

app_name = CatalogConfig.name

urlpatterns = [
    path('', product_list, name='home'),
    path('contacts/', contact_list, name='contacts')
]