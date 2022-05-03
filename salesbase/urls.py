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
from users.views import RegisterUserView
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from accounts.views import DashboardAccountsListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('', auth_views.LoginView.as_view(template_name='users/login.html',redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('dashboard/', login_required(DashboardAccountsListView.as_view()), name='dashboard'),
    # path('dashboard/', login_required(TemplateView.as_view(template_name='dashboard.html')), name='dashboard'),
    path('accounts/', include('accounts.urls'), name='accounts'),
]

    # path('', AccountsListView.as_view(), name='account-list-view'),