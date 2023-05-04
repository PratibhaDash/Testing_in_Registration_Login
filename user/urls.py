from django.urls import path
from . import views



urlpatterns = [  
        path('', views.Registrationpage, name="registration"),
        path('login/', views.Loginpage, name="login"),
        path('logout/', views.Logoutpage, name="logout"),  
    ]