from __future__ import absolute_import

from celery import Celery
from celery.utils.log import get_task_logger
from config import Config

def get_task_modules():
    with file('task.cfg') as f:
        cfg = Config(f)
        tasks = cfg.datatasks
        return list(set([x.get('module') for x in tasks]))

celeryInst = Celery(include = get_task_modules())

celeryInst.config_from_object('celeryconfig')

if __name__ == '__main__':
    celeryInst.start()

