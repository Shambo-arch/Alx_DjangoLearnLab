from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect

def is_admin(user):
    """
    Check if the user is authenticated and has the 'Admin' role.
    """
    if not user.is_authenticated:
        return False
    try:
        return user.userprofile.role == 'Admin'
    except AttributeError:
        # Handle case where UserProfile is missing
        return False

@user_passes_test(is_admin, login_url='/login/')  # Redirect to login page if not authorized
def admin_view(request):
    """
    Render the Admin view.
    """
    return render(request, 'admin_view.html', {"message": "Welcome to the Admin page!"})

