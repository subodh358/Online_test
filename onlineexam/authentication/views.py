from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth import login, authenticate
 
from .forms import SignUpForm


def std_sign_in(request):
    return render(request, 'std_sign_in.html')

def std_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'std_register.html', { 'form' : form })




















def tchr_sign_in(request):
    return render(request, 'tchr_sign_in.html')

def tchr_register(request):
    return render(request, 'tchr_register.html')