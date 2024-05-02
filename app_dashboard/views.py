from django.shortcuts import render

def home_view(request):
    return render(request, 'global/login.html', context= {
        'title': 'Dashboard',
    })