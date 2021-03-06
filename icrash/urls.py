"""icrash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path

from dashboard import views as dashboardViews
from api import views as APIViews

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'emergency_service_info', APIViews.EmergencyServiceViewSet, basename='emergency_service_info')
router.register(r'crash_points', APIViews.CrashPointViewSet, basename='crash_point')

urlpatterns = [
    path('', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('api/', include(router.urls)),
    path('', dashboardViews.home),
    path('demo', APIViews.demo),
    path('user_list', APIViews.get_user_list),
    path('emergency_contact_list', APIViews.get_emergency_contacts),
    path('login_device', APIViews.login_device, name='login_device'),
    path('add_device', APIViews.add_device, name='add_device'),
    path('add_emergency_contact', APIViews.add_emergency_contact, name='add_emergency_contact'),
    path('edit_user_info', APIViews.edit_user_info, name='edit_user_info'),
    path('log_crash', APIViews.log_crash, name="log_crash"),
]
