"""salesbase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import ContactsListView, ContactsDetailView, CreateContactsView, UpdateContactsView, DeleteContactsView


urlpatterns = [
    path('', login_required(ContactsListView.as_view()), name='contacts-list-view'),
    path('<int:pk>-<str:slug>', login_required(ContactsDetailView.as_view()), name='contacts-detail-view'),
    path('create/', login_required(CreateContactsView.as_view()), name='create-contact'),
    path('<int:pk>/update/', login_required(UpdateContactsView.as_view()), name='update-contact'),
    path('<int:pk>/delete/', login_required(DeleteContactsView.as_view()), name='delete-contact'),
]
