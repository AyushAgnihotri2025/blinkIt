from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ImageForm

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save()
                password = form.cleaned_data['password']
                user.set_password(password)
                user.save()
                auth_user = authenticate(username=user.username, first_name=user.first_name, last_name=user.last_name, email=user.email, password=password)
                if auth_user is not None:
                    login(request, auth_user)
                    return redirect('upload_image')
        else:
            form = UserForm()
        return render(request, 'signup.html', {'form': form})
    else:
        return redirect("upload_image")

def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('upload_image')
        return render(request, 'signin.html')
    else:
        return redirect("upload_image")

@login_required(login_url='/signin/')
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return JsonResponse({"url": image.image.url})
    else:
        form = ImageForm()
    images = request.user.image_set.all()
    return render(request, 'upload_image.html', {'form': form, 'images': images})
