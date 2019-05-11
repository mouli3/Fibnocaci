from django.http import JsonResponse
from django.views.generic import (
    CreateView, UpdateView, DetailView, TemplateView, View, DeleteView)
class Fibonacci()

    n = int(input("Enther thr  nth Number"))

    def Fibonacc(n):
        if n < 0:
            return ("Incorrect input")
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return ((Fibonacc(n - 1) + Fibonacc(n - 2)))

    print(Fibonacc(n))