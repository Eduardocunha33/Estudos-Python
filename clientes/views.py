from django.shortcuts import render
from django.http import HttpResponse
def cliente(request):
    return HttpResponse("Olá, mundo! Este é o cliente.")