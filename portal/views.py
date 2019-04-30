from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'portal/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'portal/signup.html', {'form': form})

