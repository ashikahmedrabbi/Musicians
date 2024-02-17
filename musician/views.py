from django.shortcuts import render, redirect
from . import forms




def add_musician(request):
    if request.method == 'POST':
        profile_form = forms.MusicianForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('add_musician')
    
    else:
        add_musician = forms.MusicianForm()
    return render(request, 'add_musician.html', {'form' : add_musician})
