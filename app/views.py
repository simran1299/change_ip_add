from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_host(request):
    return HttpResponse('first_host')