# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hey what's up!<h1>")


def country_order(request, country_id):
    return HttpResponse("<h2>This is country number %s<h2>"%str(country_id))
