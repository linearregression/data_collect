# -*- coding: utf-8 -*-

from __future__ import absolute_import

from celery import Celery

# instantiate 
collect_facebook_worker =  Celery( include = ['tasks.collect_facebook'])

# import celery config
collect_facebook_worker.config_from_object('celeryconfig')

# start worker instance

if __name__ == '__main__':
    collect_facebook_worker.start()


