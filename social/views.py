from django.shortcuts import render

def home(request):
    return render(request, 'social/home.html', {})

def register_practitioner(request):
    return render(request, 'social/register_practitioner.html', {})

def register_consultee(request):
    return render(request, 'social/register_consultee.html', {})
