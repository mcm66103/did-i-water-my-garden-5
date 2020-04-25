from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import NewAccountForm

# Create your views here.
def create_account(request):
    if request.method == 'POST':
        form = NewAccountForm(data=request.POST)
        if form.is_valid():
            new_account = form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=raw_password)
            login(request, user)
            return redirect('/plants/')
    else:
        form = NewAccountForm()
    return render(request, 'create_account.html', {'form': form})
