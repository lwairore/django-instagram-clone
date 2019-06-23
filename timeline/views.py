from django.shortcuts import render, redirect
from homepage.models import Image, Follow
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login')
def timeline_page(request):
    pass
