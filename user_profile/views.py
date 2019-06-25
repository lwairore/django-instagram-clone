from django.shortcuts import render, redirect
from homepage.models import Image, Follow
from django.contrib.auth.decorators import login_required
from .forms import NewProfileForm, NewImageForm
from homepage.models import Profile

# Create your views here.
@login_required(login_url='/accounts/login')
def edit_profile_page(request):
    current_user = request.user
    print('-'* 40)
    print(current_user.id)
    all_images = Image.objects.all()
    all_instagram_followers = Follow.objects.all()
    following = Follow.objects.filter(user_id=current_user.id)
    print('=>'*10, following.count())
    user_images = []
    for j in all_images:
        if j.uploaded_by==current_user:
            print(j.uploaded_by)
            user_images.append(j.image)
    print('+' * 30)
    print(user_images)
    form = NewProfileForm(request.POST, request.FILES)
    all_profile = Profile.objects.filter(user_id=current_user.id)
    print('--->' * 30)
    print(all_profile)
    user_name = current_user

    if Profile.objects.filter(user_id=current_user.id):
        profile_personal = Profile.objects.filter(user_id=current_user.id)
        print('--->' * 30)
        return render(request, 'profile/edit_user_profile_page.html', {'form':form, 'user_images':user_images, 'following':following.count(), 'user_name':user_name, 'profile_personal':profile_personal})


    
    return render(request, 'profile/edit_user_profile_page.html', {'form':form, 'user_images':user_images, 'following':following.count(), 'user_name':user_name})

@login_required(login_url='/accounts/login')
def profile_page(request):
    current_user = request.user
    print('-'* 40)
    print(current_user.id)
    all_images = Image.objects.all()
    all_instagram_followers = Follow.objects.all()
    following = Follow.objects.filter(user_id=current_user.id)
    print('=>'*10, following.count())
    user_images = []
    for j in all_images:
        if j.uploaded_by==current_user:
            print(j.uploaded_by)
            user_images.append(j.image)
    print('+' * 30)
    print(user_images)
    return render(request, 'profile/profile_page.html', {'user_images':user_images, 'following':following.count()})

def new_image(request):
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        current_user = request.user
        image = form.save(commit=False)
        image.uploaded_by = current_user
        image.save()
        if form.is_valid():
            image = form.save(commit=False)
            image.uploaded_by = current_user
            image.save()
            image.save_image()
    
    return redirect(edit_profile_page)

@login_required(login_url='/accounts/login')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST'  :
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        print('*' * 30)
        print(bio)
        print('*' * 30)
        print(first_name, last_name, phone, email)
        user_id = current_user.id
        if Profile.objects.filter(user_id=user_id):
            user = Profile.objects.filter(user_id=user_id)
            user.first_name = first_name
            user.last_name = last_name
            user.phone = phone
            user.email = email
            user.bio = bio
            form = NewProfileForm(request.POST, request.FILES)
            if form.is_valid():
                form = form.save()
        
            print('*' * 30)
            # print(user)
            user.update()
        else: 
            new_profile = Profile.objects.create(user_id=current_user.id, first_name=first_name, last_name=last_name,email=email,phone=phone, bio=bio)
    return redirect(edit_profile_page)
        