from django.shortcuts import render
from .models import Topic
# from django.http import HttpRequest

# Create your views here.
def index(request):
    # вывод общей информации
    return render(request, 'index.html')

def topics(request):
    """Вывод списка тем для обучений"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)

def topic(request, topic_id):
    """Выводит одну тему и все её записи"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'topic.html', context)
