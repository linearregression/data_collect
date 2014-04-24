"""
    Get Handles from Riak Storage.  
"""

import riak
import uuid
import logging import __get_logger__
from __future__ import absolute_import

from time import sleep

from celery.contrib.methods import task_method

class GetStoredHandles(object):

    """Fetch the handles stored. No more reading from Flat files"""    
    def __init__(self, task, *args, **kawrgs):
        self.task = task

    def get_handle(self, Connection):



def task(*args, **kwargs):
    return current_app.task(*args, **dict(kwargs, filter=task_method))

