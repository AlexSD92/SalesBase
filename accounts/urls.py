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
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import AccountsListView, AccountsDetailView, CreateAccountsView, UpdateAccountsView, DeleteAccountsView


urlpatterns = [
    path('', login_required(AccountsListView.as_view()), name='account-list-view'),
    path('<int:pk>-<str:slug>', login_required(AccountsDetailView.as_view()), name='accounts-detail-view'),
    path('create/', login_required(CreateAccountsView.as_view()), name='create-account'),
    path('<int:pk>/update/', login_required(UpdateAccountsView.as_view()), name='update-account'),
    path('<int:pk>/delete/', login_required(DeleteAccountsView.as_view()), name='delete-account'),
]
