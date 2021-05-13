from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from inv_profiles.models import Profile


def create_user(request):
    """
        Show a user registration form and create a new user account 
        if the data provided in the form is valid
    """
    success = False

    if request.POST:
        form = UserCreationForm(request.POST)

        # Keep these lines for debugging purposes
        print("===============================")
        print("RECEIVED POST REQUEST TO CREATE A NEW ACCOUNT")
        print("===============================")
        print()
        print("The data is the following:")
        print(form)

        if form.is_valid():
            print("-> Form IS valid, creating a new account.")
            print()
            form.save()
            success = True
        else:
            print("-> Form is NOT valid, not creating account.")
            print()
    else:
        form = UserCreationForm()

    return render(request, 'user_management/register.html',
                    {'success': success,
                     'form': form}
                 )


def login_user(request):
    """ Log in a user based on a given username and password """
    success = False
    failure = False
    form = 0
    
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        form = AuthenticationForm(data=request.POST)

        # We first authenticate the user to check
        # if the credentials are correct
        user = authenticate(username=username, password=password)

        if user is not None:
            success = True
            print("User is authenticated!")
            login(request, user)
            print("User is logged in")
            print(user)
            return redirect('info:index')
        else:
            failure = True
            print("User provided incorrect username and password")

    return render(request, 'user_management/login.html',
                  {'success': success,
                   'failure': failure,
                   'form': form})


def logout_user(request):
    logout(request)
    return redirect('info:index' )


def user_profile(request):
    return render(request, 'user_management/user_profile.html')


def delete_user(request):
    pass


def disable_user(request):
    pass


def edit_user_information(request):
    pass


def reset_password(request):
    pass


def user_investment_profiles(request):
    user_logged_in = True

    if request.user:
        user = request.user
        inv_profiles = Profile.objects.filter(user=user)
    else:
        user_logged_in = False

    return render(request, 'user_management/user_investment_profiles.html',
                  {'inv_profiles': inv_profiles,
                   'user_logged_in': user_logged_in})


def user_shared_profiles(request):
    user_logged_in = True
    shared_profiles = True

    if request.user:
        user = request.user
        inv_profiles = Profile.objects.filter(user=user)
        shared_inv_profiles = inv_profiles.filter(shared=True)

        if shared_inv_profiles:
            shared_profiles = True
    else:
        user_logged_in = False

    return render(request, 'user_management/user_shared_profile.html',
                  {'shared_inv_profiles': shared_inv_profiles,
                   'user_logged_in': user_logged_in,
                   'shared_profiles': shared_profiles})


def user_shared_ideas(request):
    return render(request, 'user_management/user_shared_ideas.html')


def user_groups(request):
    pass


def user_permissions(request):
    pass


def user_settings(request):
    pass
