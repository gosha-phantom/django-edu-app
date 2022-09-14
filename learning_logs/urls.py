from django.urls import include, re_path
from . import views

urlpatterns = [
    # домашняя страница
    re_path(r'^$', views.index, name='index'),
    # страница с темами для обучения
    re_path(r'^topics/$', views.topics, name='topics'),
    # страница с подробной информацией по выбранной теме
    re_path(r'^topics/(?P<topic_id>\d+$)', views.topic, name='topic')
]
