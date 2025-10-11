from django.urls import path
from .views import contact_list, contact_detail, ContactView

urlpatterns = [
    path('contacts/', contact_list),
    path('contacts/<int:id>/', contact_detail),
    path('contact_apiview/', ContactView.as_view()),
    path('contact_apiview/<int:id>/', ContactView.as_view()),
    
]
