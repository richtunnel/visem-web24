from frontend.views import views
from django.urls import path

app_name = "frontend"

urlpatterns = [
    
    path("", views.HomePageView.as_view(), name="index"),
    path("founder/portfolio/", views.RicksPortfolio.as_view(), name="ricks_resume")
    
    
]
