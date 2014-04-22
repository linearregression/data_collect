# -*- coding: utf-8 -*-
"""Concrete Task for Followers to facebook profile data collection"""

import json
import oauth2
import gc
import requests
import task_base


class CollectFacebook(TaskCollect):
    """Concrete Class to implement Facebook Follower Task, derives from Task_Base."""
    
    default_access_token = "733753326637318|v5JLdgJ48ST2Qzo0ujoKz7azv_o"

    def __init__(self, Context):



    @abc.abstractmethod
    def report_status(self):
        """Report current progress status of task. """
        raise NotImplementedError()

    @abc.abstractmethod
    def store(self):
        """Action to store the result. """
        raise NotImplementedError()

    @abc.abstractmethod
    def remove_context(self):
        """Perform any clean up work to delete this context. """
        raise NotImplementedError()

    @task_postrun.collect 
    def collect_after_task(**kwargs): 
        gc.collect() 
