from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# from django.contrib import messages

@login_required
def logout_view(request):
    """Страница завершения сеанса пользователя"""
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    """Регистрирует нового пользователя"""
    if request.method != 'POST':
        # показать пустую форму регистрации
        form = UserCreationForm()
    else:
        # обработка заполненной формы
        form = UserCreationForm(data = request.POST)

        if form.is_valid():
            new_user = form.save()
            # выполнение входа и перенаправление на домашнюю страницу
            authenticated_user = authenticate(username = new_user.username,
                                                password = request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))
    context = {'form': form}
    return render(request, 'register.html', context)



