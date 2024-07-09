"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

# Pip imports
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

# Internal imports
from core import views


admin.site.site_header = f'[{settings.ENVIRONMENT}] BaheaCal Admin'


def trigger_error(request):
    _ = 1 / 0


urlpatterns = [
    path("admin/", admin.site.urls),
    path("calendar/init/", views.google_calendar_init_view, name="google_permission"),
    path("calendar/redirect/", views.google_calendar_redirect_view, name="google_redirect"),
    path("calendar/success/", views.google_calendar_success, name="google_success"),
    path("", views.home, name="home"),
    path("privacidade/", TemplateView.as_view(template_name='core/privacy.html')),
    path("termos/", TemplateView.as_view(template_name='core/terms.html')),
    path("user/", include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
    path('sentry-debug/', trigger_error),
]
