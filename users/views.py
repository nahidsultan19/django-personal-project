from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created!You are now able to login')
            return redirect('login')

    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'register.html', context)
