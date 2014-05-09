# -*- coding: utf-8 -*-
"""Abstract Base Class for Task"""

import abc

class TaskCollect(__metaclass__ = abc.ABCMeta):
    """Abstract Base Class for Task"""

    @abc.abstractmethod
    def init_context(self, context):
        """Initialize task context. e.g handle source, result storage, api key etc. """
        raise NotImplementedError()

    @abc.abstractmethod
    def get_task_info(self):
        """Return task info. environment, jobId, who is running it, instance name, ip, etc. """
        raise NotImplementedError()

    @abc.abstractmethod
    def get_handles(self):
        """Return list of handles to be processed. """
        raise NotImplementedError()

    @abc.abstractmethod
    def get_next_handle(self):
        """Return handle next in queue to be process etc """
        raise NotImplementedError()

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

