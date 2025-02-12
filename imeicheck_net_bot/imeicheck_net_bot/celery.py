import os
from celery import Celery
from celery.schedules import crontab
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'imeicheck_net_bot.settings')
 
app = Celery('imeicheck_net_bot')
app.config_from_object('django.conf:settings', namespace = 'CELERY')
# app.conf.beat_schedule = {
#     'ts_sending_out_new_posts': {
#         'task': 'news.tasks.ts_sending_out_new_posts',
#         'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
#         # 'schedule': crontab(hour=17, minute=35),
#         'args': (),
#     },
# }
app.autodiscover_tasks(['imeicheck_bot'])