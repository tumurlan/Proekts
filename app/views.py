from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm
from rest_framework import generics
from .serializers import *
from .permissions import IfIsOwner
from rest_framework.permissions import IsAuthenticated, IsAdminUser

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

class ClientCreateView(generics.CreateAPIView):
    serializer_class = ClientSerializers
    permission_classes = [IsAdminUser, ]

class ClientListView(generics.ListAPIView):
    serializer_class = ClientSerializers
    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticated, ]

class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientDetailSerializers
    queryset = Feedback.objects.all()
    # permission_classes = [IfIsOwner, IsAuthenticated]