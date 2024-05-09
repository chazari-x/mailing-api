import os
from celery import Celery
from celery.schedules import crontab

# Указываем Django-приложение для настроек Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings')

# Создаем экземпляр приложения Celery
app = Celery('project_name')

# Загружаем конфигурацию из настроек Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находим и регистрируем задачи
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-scheduled-mail-every-minute': {
        'task': 'polls.tasks.send_scheduled_mail',
        'schedule': crontab(minute='*'),
    }
}

app.conf.timezone = 'UTC'

