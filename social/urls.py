from django.urls import path
#desde este directorio hace referencia a las vistas de la carpeta
from . import views 
urlpatterns = [
    path('',views.feed, name='feed'),
    path('profile/', views.profile, name ='profile'),
]
