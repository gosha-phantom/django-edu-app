import re
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Entry, Topic
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    # вывод общей информации
    return render(request, 'index.html')


@login_required
def topics(request):
    """Вывод списка тем для обучений"""
    # topics = Topic.objects.order_by('date_added')
    topics = Topic.objects.filter(owner = request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)


@login_required
def topic(request, topic_id):
    """Выводит одну тему и все её записи"""
    topic = Topic.objects.get(id=topic_id)
    # проверка того, что тема принадлежит текущему пользователю
    # if topic.owner != request.user:
    #     raise Http404
    check_topic_owner(topic.owner, request.user)

    entries = topic.entry.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'topic.html', context)


@login_required
def new_topic(request):
    """Опрделяет новую тему для обучения"""
    if request.method != 'POST':
        # данные не отправлялись, создается пустая форма
        form = TopicForm()
    else:
        # отправлены данные из формы, необходимо обработать
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit = False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('topics'))
    
    context = {'form': form}
    return render(request, 'new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Добавляет новую запись по конкретной теме"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # данные не отправлялись, создается пустая форма
        check_topic_owner(topic.owner, request.user)
        form = EntryForm()
    else:
        # отправлены данные из формы, необходимо обработать
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    
    context = {'topic': topic, 'form': form}
    return render(request, 'new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Изменяет запись по конкретной теме"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # if topic.owner != request.user:
    #     raise Http404
    check_topic_owner(topic.owner, request.user)

    if request.method != 'POST':
        # данные не отправлялись, создается пустая форма
        form = EntryForm(instance=entry)
    else:
        # отправлены данные из формы, необходимо обработать
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'edit_entry.html', context)


def check_topic_owner(user, owner):
    """проверяем принадлежность пользователю"""
    if owner != user:
        raise Http404