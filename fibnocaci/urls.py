from django.urls import path
urlpatterns = [
    path('Nthnumber/', Fibonacci.as_view(), name='Nthnumber')]