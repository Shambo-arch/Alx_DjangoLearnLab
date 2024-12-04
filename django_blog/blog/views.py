from django.shortcuts import render
# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# Registration view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login view (using built-in Django view)
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout view
def user_logout(request):
    logout(request)
    return redirect('login')

# Profile view and edit
@login_required
def profile(request):
    if request.method == 'POST':
        # Update user's email
        user = request.user
        user.email = request.POST.get('email')
        user.save()  # Save the updated user instance
        return redirect('profile')  # Redirect to the profile page after saving
    return render(request, 'profile.html', {'user': request.user})

