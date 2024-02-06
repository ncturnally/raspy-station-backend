"""
URL configuration for raspy-station-backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.raspy-station-backend, name='raspy-station-backend')
Class-based views
    1. Add an import:  from other_app.views import raspy-station-backend
    2. Add a URL to urlpatterns:  path('', raspy-station-backend.as_view(), name='raspy-station-backend')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
