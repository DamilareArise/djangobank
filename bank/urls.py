"""
URL configuration for bank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from app.views import homeView, aboutView, deleteUser, editUser
from userApp.views import SignupView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', homeView, name='home'),
    path('about/', aboutView, name='about'),
    path('delete-user/<int:id>/', deleteUser, name='delete-user'),
    path('edit-user/<int:id>/', editUser, name="edit-user"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup', SignupView.as_view(), name='signup'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
