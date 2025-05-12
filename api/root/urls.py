"""
URL configuration for root project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import CookieTokenObtainPairView, CookieTokenRefreshView, LogoutView

API_PREFIX = "api/"

urlpatterns = [
    path(f"{API_PREFIX}login/", CookieTokenObtainPairView.as_view(), name="login"),
    path(f"{API_PREFIX}refresh/", CookieTokenRefreshView.as_view(), name="refresh_token"),
    path(f"{API_PREFIX}logout/", LogoutView.as_view(), name="logout"),
    path(f"{API_PREFIX}admin/", admin.site.urls),
    path(f"{API_PREFIX}user/", include("user.urls")),
    path(f"{API_PREFIX}cms/", include("cms.urls")),
]
