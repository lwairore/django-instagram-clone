from django.shortcuts import render, redirect


# Create your views here.
def edit_profile_page(request):
    return render(request, 'profile/edit_user_profile_page.html')

# def profile_page(request):