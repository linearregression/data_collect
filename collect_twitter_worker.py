from __future__ import absolute_import

from celery import Celery

# instantiate 
collect_twitter_worker =  Celery( include = ['tasks.collect_twitter'])

# import celery config
collect_twitter_worker.config_from_object('celeryconfig')

#start

if __name __ == '__main__':
    collect_twitter_worker.start()

