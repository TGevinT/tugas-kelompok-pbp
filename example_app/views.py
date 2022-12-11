from django.shortcuts import render

def index(request):

    context = {
        'login_status': 'hidden',
        'register_status': 'hidden',
        'logout_status': 'hidden',
    }

    return render(request, 'index.html', context)
