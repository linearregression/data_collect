from __future__ import absolute_import

from celery import Celery

# instantiate 
collect_instagram_worker =  Celery( include = ['tasks.collect_instagram'])

# import celery config
collect_instagram_worker.config_from_object('celeryconfig')

#start

 if __name __ == '__main__':
    collect_instagram_worker.start()

