from django.urls import path
from .views import contact_list, contact_detail

urlpatterns = [
    path('contacts/', contact_list),
    path('contacts/<int:id>/', contact_detail),
]
