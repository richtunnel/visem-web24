
from django.urls import path, include
from django.contrib import admin

urlpatterns = []

urls = [
    # Django admin
    path("admin/", admin.site.urls),
    #path("api/", include("backend.urls")),
    # User management
    # Buyable frontends
    # Dealership frontends

    # Landing page, partner page, privacy policy pages, and etc.
    path("", include( "frontend.urls", namespace="frontend")),
    
]

urlpatterns.extend(urls)
