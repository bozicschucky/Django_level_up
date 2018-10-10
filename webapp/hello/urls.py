from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<name>', views.hello_there, name='Hello there'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('log/', views.log_message, name='log'),
]
