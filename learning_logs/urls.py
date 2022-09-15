from django.urls import include, re_path
from . import views

urlpatterns = [
    # домашняя страница
    re_path(r'^$', views.index, name = 'index'),
    # страница с темами для обучения
    re_path(r'^topics/$', views.topics, name = 'topics'),
    # страница с подробной информацией по выбранной теме
    re_path(r'^topics/(?P<topic_id>\d+$)', views.topic, name = 'topic'),
    # страница для добавления новой темы
    re_path(r'^new_topic/$', views.new_topic, name = 'new_topic'),
    # страница для добавления новой записи
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name = 'new_entry'),
    # страница для редактирования записи
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name = 'edit_entry')
]
