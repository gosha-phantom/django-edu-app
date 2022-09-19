from django.urls import re_path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'

urlpatterns = [
    # страница авторизации пользователя
    re_path('login/$', LoginView.as_view(template_name = 'login.html'), name = 'login'),
    # страница выхода пользователя
    re_path('logout/$', views.logout_view, name = 'logout_view'),
    # страница регистрации нового пользователя
    re_path('register/$', views.register, name = 'register')
    
]
