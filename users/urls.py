from django.urls import re_path
from django.contrib.auth.views import LoginView

app_name = 'users'

urlpatterns = [
    # страница авторизации пользователя
    re_path(r'^login/$', LoginView.as_view(template_name = 'login.html'), name = 'login')
    # re_path('login/$', views.login, name = 'login')
    # страница выхода пользователя
    # re_path('logout/$', views_logout, name = 'logout_view')
    
]
