from django.contrib.auth import logout
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from .forms import RegistrationForm
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from hunt.models import *

def main_index(request):
    return render(request,'main_index.html')

def custom_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/hunt')
    else:
        return login(request)

def logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })

    return render_to_response(
    'registration/register.html',
    variables,
    )

def register_success(request):
    successfull_registration="You have successfully registered."
    return render_to_response(
    'registration/success.html', {'msg':successfull_registration})
