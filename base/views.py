from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')
def testing(request):
    return render(request, 'testing.html')