from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib.auth import logout
from django.shortcuts import redirect


"""
Class-based views:

View         = Generic View
ListView     = get a list of records
DetailView   = get a single (detail) record
CreateView   = create a new record
DeleteView   = remove a record
UpdateView   = modify an existing record
LoginView    = LogIn

"""


# Create your views here.
class UserLogin(LoginView):
    template_name = 'users/login.html'

class UserSignup(CreateView):
    model= User
    form_class = SignupForm #use the form created in forms.py
    template_name = 'users/signup.html' #signup template is here
    success_url = '/users/login/'  # Redirect to login page after successful signup

    def form_valid(self, form):
        # Save the new user
        user = form.save(commit=False) # extract user data but don't save yet
        pass_text = form.cleaned_data['password'] # get the password from the form
        user.set_password(pass_text) # encrypts the password
        user.save() # saves the user to the database
        
        return super().form_valid(form)
    


def logout_view(request):
    logout(request)
    request.session.flush()  # Clears session data including cached user info
    return redirect('home')