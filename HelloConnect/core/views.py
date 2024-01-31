from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.



def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {'form': form})



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('frontpage')
        else:
            # Handle invalid login attempt
            # For example, add error message to context and render login form again
            context = {'error_message': 'Invalid username or password.'}
            return render(request, 'core/login.html', context)
    else:
        # Render the login form
        return render(request, 'core/login.html')




@login_required
def profile_view(request):
    # View logic for the profile page
    return render(request, 'core/profile.html') 