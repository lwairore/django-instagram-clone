from django.shortcuts import render, redirect
from .forms import NewImageForm, SignupForm
from .models import Image, Follow
from django.http import HttpResponse
# from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.views.decorators.csrf import ensure_csrf_cookie


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
    return render(request, 'suggestions/suggestions.html', {'title':title, 'images':images})

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
    else:
        form = NewImageForm()
    return render(request, 'image/new_image.html', {'form':form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('<body style="background: #e2e2e2;">Thank you for your email confirmation. Now you can <a href="/accounts/login/">login</a> your account.</body>')
    else:
        return HttpResponse('Activation link has expired!')


# @ensure_csrf_cookie
def follow(request, following_id):
    current_user = request.user
    trial = User.objects.get(username=current_user).pk
    # print('->'*5,trial)
    # print('+' * 30)
    # print(current_user)
    if request.method == 'POST':
        trial_id = current_user.id
        # print(type(trial_id))
        # new_follower = Follow(user_id=0, following_id=0)
        # Follow.objects.create(user_id=0, following_id=0)
        # user = User.objects.get(id=trial_id)
        # print('+' * 30)
        # print(user.id)
        # new_follower = Follow(user_id=trial)
        # new_follower = Follow.objects.create(user_id=trial)
        # print('='*10,new_follower.user_id)
        # print(new_follower)
        # new_follower.save()
        # new_follower.save()
        # new_follower.save()
        new_follower = Follow.objects.create(user_id=trial, following_id=following_id)
    # return redirect(index)
    return redirect(index)
    # return render(request, 'signup.html')


        # being_followed_id = 


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
                # searched_users = User.objects.filter(username=)
                # post_images = Im
        return redirect(index)


    


