import config
from config import Config
from __future__ import absolute_import
from celery import Celery

def get_task_modules():
    with file('task.cfg') as f:
        cfg = Config(f)
        tasks = cfg.datatasks
        return list(set([x.get('module') for x in tasks]))

celery = Celery(include = get_task_modules())

celery.config_from_object('celeryconfig')


