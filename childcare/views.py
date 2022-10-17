from django.shortcuts import render

# Create your views here.
def show_childcare(request):
    return render(request, 'childcare.html')