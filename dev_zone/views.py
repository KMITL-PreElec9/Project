from django.shortcuts import render
from django.http import HttpResponseRedirect
from dev_zone.forms import ContactForm

def index(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
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