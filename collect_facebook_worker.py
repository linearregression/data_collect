from __future__ import absolute_import

from celery import Celery

# instantiate 
collect_facebook_worker =  Celery( include = ['task.facebook_collect_task'])

# import celery config
collect_facebook_worker.config_from_object('celeryconfig')

#start

 if __name __ == '__main__':
    collect_facebook_worker.start()

