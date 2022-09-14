from django.contrib import admin

# Register your models here.
# регистрируем модель БД отдельных топиков
from learning_logs.models import Topic
admin.site.register(Topic)

# регистрируем модель БД изучений топиков
from learning_logs.models import Entry
admin.site.register(Entry)