from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# from django.contrib.auth import login, logout, authenticate
# from django.contrib import messages


# Create your views here.
# def login(request):
#     """Страница авторизации пользователя"""
#     # return render(request, 'login.html')
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user != None:
#             login(request, user)
#             return HttpResponseRedirect(reverse(''))
#         else:
#             messages.info(request, 'Username or Password is incorrect')
#     context = {}
#     return render(request, 'login.html', context)
    # template_name = 'login.html'


# def logout_view(request):
#     """Страница завершения сеанса пользователя"""
#     logout(request)


