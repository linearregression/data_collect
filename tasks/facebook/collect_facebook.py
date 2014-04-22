# -*- coding: utf-8 -*-
"""Concrete Task for Facebook data collection"""

import json
import oauth2
import gc
import requests
import task_base


class CollectFacebook(TaskCollect):
    """Concrete Class to implement Facebook Data Collection Task, derives from Task_Base."""
    
    default_access_token = "733753326637318|v5JLdgJ48ST2Qzo0ujoKz7azv_o"

    def __init__(self, Context):

    @task_postrun.collect 
    def collect_after_task(**kwargs): 
        gc.collect() 
