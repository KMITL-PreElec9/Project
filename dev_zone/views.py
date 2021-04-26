from django.shortcuts import render
from django.http import HttpResponseRedirect
from dev_zone.forms import ContactForm
from .models import Data
from django.utils import timezone

def index(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            db = Data(name = cd['yourname'], email =cd['email'], subject = cd['subject'], \
                message = cd['message'], datetime = timezone.now())
            db.save()
            return render(request, 'dev_zone/index.html', 
                {
                    'form': form, 
                    'submitted': True,
                    'name': cd['yourname'],
                    'email': cd['email'],
                    'subject': cd['subject'],
                    'message': cd['message'],
                    })
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True 
    return render(request, 'dev_zone/index.html', {'form': form, 'submitted': submitted})

def show_data(request):
    getdata = Data.objects.all()
    return render(request, 'dev_zone/showdata.html', {'data': getdata})