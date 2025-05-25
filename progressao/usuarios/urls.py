from django.urls import path
from django.contrib.auth import views as auth_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/',auth_view.LoginView.as_view(
        template_name='usuarios/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
     
]


