from django.shortcuts import render
from django.http import HttpResponse
from .models import Staff_auth

def index(request):
    try:
        #output = Staff_auth.objects.get(email = '63010104@kmitl.ac.th')
        a = request.user.email
    except:
        a = 'Error'    
    return HttpResponse(a)

def test(request):
    return render(request, 'test.html')