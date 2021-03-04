from django.shortcuts import render

# Create your views here.
#creacion del feed funcion
def feed(request):
    return render(request, 'social/feed.html')

#creacion de funcion de perfil

def profile(request):
    return render(request, 'social/profile.html')