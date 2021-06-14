"""overbergsalon URL Configuration

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
from django.urls import path, include, re_path
from home import views as home_views

urlpatterns = [
    path('', include("home.urls")),
    path('admin/', admin.site.urls),
    re_path(r"^Pricing/?$", home_views.pricing_list, name="price-page"),
    re_path(r"^Products/?$", home_views.product_list, name="product-page"),
    re_path(r"^Portfolio/?$", home_views.portfolio, name="portfolio-page"),
    re_path(r"^Contact/?$", home_views.contact_us, name="contact-page"),

 ]
