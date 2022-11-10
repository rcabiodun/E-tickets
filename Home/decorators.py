from django.shortcuts import render, redirect

def authenticatedusers(func):
    def inner(request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return func(request)

    return inner