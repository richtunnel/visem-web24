from frontend.views import views
from django.urls import path

app_name = "frontend"

urlpatterns = [
    
    path("", views.HomePageView.as_view(), name="index")
    
    
]
