from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    title = 'Instagram'
    return render(request, 'suggestions.html', {'title':title})