# -*- coding: utf-8 -*-

from __future__ import absolute_import

from celery import Celery

# instantiate 
collect_news_worker =  Celery( include = ['tasks.collect_news'])

# import celery config
collect_news_worker.config_from_object('celeryconfig')

#start

if __name__ == '__main__':
    collect_news_worker.start()

