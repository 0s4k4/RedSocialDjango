from django.shortcuts import render
from .models import *

# Create your views here.
#creacion del feed funcion
def feed(request):
    #se mandan a llamar todos los post
    posts = Post.objects.all()
    #se pasan todos los post con la funcion de context
    context = {'post': posts}
    return render(request, 'social/feed.html')

#creacion de funcion de perfil

def profile(request):
    return render(request, 'social/profile.html')