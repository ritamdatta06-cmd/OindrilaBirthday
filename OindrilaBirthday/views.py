from django.shortcuts import render,redirect
from .models import BirthdayWish
from .forms import BirthdayWishForm

def landing_page(request):
    return render(request, 'landing_page.html')

def cakecut(request):
    return render(request, 'cakecut.html')

def birthday(request):
    name = "Oindrila"
    message = "Wishing you a very Happy Birthday!"
    return render(request, 'birthday.html', {'name': name, 'message': message})

def thank_you(request):
    if request.method == 'POST':
        form = BirthdayWishForm(request.POST)
        if form.is_valid():
            guest_name = form.cleaned_data['guest_name']
            note = form.cleaned_data['note']
            BirthdayWish.objects.create(guest_name=guest_name, text=note)
            return redirect('final')
    else:
        form = BirthdayWishForm()

    return render(request, 'thank_you.html', {'form': form})

def final(request):
    return render(request, 'final.html')
