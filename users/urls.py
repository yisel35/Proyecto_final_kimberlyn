from django.urls import path, reverse_lazy
from users import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('login/', views.login_request, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
    ]