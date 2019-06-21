from django.shortcuts import render, redirect
from .forms import NewImageForm

# Create your views here.
def index(request):
    title = 'Instagram'
    return render(request, 'suggestions/suggestions.html', {'title':title})

def new_image(request):
    if request.method = 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.save()
        else:
            form = NewImageForm()
    return render(request, 'image/new_image.html', {'form':form})