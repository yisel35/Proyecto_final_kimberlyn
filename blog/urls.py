from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),  #inicio
    path('posts/', views.post_list, name='post_list'), #lista de publicaciones 
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'), #crear publicaion
    path('profile/', views.profile, name='profile'),  #perfil
    path('profile/edit/', views.edit_profile, name='edit_profile'), # editar perfil 
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
]

