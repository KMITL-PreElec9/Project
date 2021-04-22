from django.shortcuts import render
from django.http import HttpResponse
from .models import Staff_auth

def index(request):
    output = Staff_auth.objects.get(email = '63010104@kmitl.ac.th')
    a = request.user.email
    return HttpResponse(a)