"""
URL configuration for myapp project.

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

# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path("admin/", admin.site.urls),
# ]
from django.urls import path
from htopapp.views import htop_view
from django.http import HttpResponse

# Define the home_view function before using it
def home_view(request):
    return HttpResponse("<h1>Welcome! Go to <a href='/htop/'>/htop</a> to see system info.</h1>")

urlpatterns = [
    path('', home_view),  # Handles '/'
    path('htop/', htop_view),
]
