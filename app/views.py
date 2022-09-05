from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm

def index(request):
    return render(request, 'index.html')

def add_info(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            fb = form.save()
            return redirect('/')
    else:
        form = FeedbackForm()
    return render(request, 'index.html', {'feedback_form' : form})