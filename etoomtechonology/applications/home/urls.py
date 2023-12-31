from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    #path('quienes-somos', views.quienesSomosView.as_view(), name='quienes-somos'),  
    path('', views.HomePageView.as_view(), name='inicio'),  
    path('register-suscripcion', views.SuscribersCreateView.as_view(), name='add-suscripcion'),  
    path('contact', views.ContactCreateView.as_view(), name='add-contact'),  
]