from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import Check_question
from .models import *
# Create your views here.
#@login_required

def hunt_main_page(request):
    if request.user.is_authenticated():
        if request.method == 'POST':                            # Form is submitted by the user :b
            form = Check_question(request.POST)                 # Create an object of answer form :b
            if form.is_valid():
                given_answer = form.cleaned_data['answer']
                valid_answer = Question.objects.get(level = request.user.player.level).answer
                if valid_answer == given_answer :               # If Answer is correct
                    current_user=request.user
                    current_user.player.levelup()
                    current_user.player.save()                  # Levelup player and save the data
                    return render_to_response('hunt/success.html', {'username' : request.user.username})
                else:
                    return HttpResponseRedirect('/hunt')
        else:                                                   # If User views that page. No submissions. or GET Request
            username=request.user.get_username
            user_level = request.user.player.level
            question = Question.objects.get(level = user_level)
            form = Check_question()
            return render_to_response('hunt/hunt_index.html', {'username':username, 'level':user_level , 'question':question , 'form': form})
    else:                                                       # if user is not authenticated
        return HttpResponseRedirect('/')
