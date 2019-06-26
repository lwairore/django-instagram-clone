from django.shortcuts import render, redirect
from .forms import NewImageForm, SignupForm
from .models import Image, Follow
from django.http import HttpResponse
from django.contrib.auth.models import User
# from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_intro(request):
    return render(request, 'intro/signin.html')


@login_required(login_url='/accounts/login/')
def index(request):
    title = 'Instagram'
    images = Image.objects.all()
    images_total = images.count()
    print('='*10, images_total)
    for i in images:
        print('^'* 30)
        print(i.uploaded_by)
    print(images)
    all_users = User.objects.all()
    
    return render(request, 'suggestions/suggestions.html', {'title':title, 'images':images, 'all_users':all_users, 'current_user_id':request.user.id})

def new_image(request):
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        current_user = request.user
        if form.is_valid():
            image = form.save(commit=False)
            image.uploaded_by = current_user
            image.save()
            print('-' * 30)
            print(image.uploaded_by)
            image.save_image()
            return redirect(index)
    else:
        form = NewImageForm()
    return render(request, 'image/new_image.html', {'form':form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return HttpResponse('<body style="background: #e2e2e2;">Now you can <a href="/accounts/login/">login</a> your account.</body>')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# @ensure_csrf_cookie
def follow(request, following_id):
    current_user = request.user
    trial = User.objects.get(username=current_user).pk
    if request.method == 'POST':
        trial_id = current_user.id
        new_follower = Follow.objects.create(user_id=trial, following_id=following_id)
    return redirect(index)


def search_results(request):
    if 'search' in request.GET and request.GET['search']:
        search_term_original = request.GET.get('search')
        search_term = search_term_original.lower()
        all_users = User.objects.all()
        users_final = []

        for i in all_users:
            if search_term == i.username.lower():
                print('-'* 20)
                print("hello")
        return redirect(index)


    


