import abc

class TaskCollect(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def init_context(self, context):
        """Initialize task context. e.g handle source, result storage, api key etc. """
        return

    @abc.abstractmethod
    def get_task_info(self):
        """Return task info. environment, jobId, who is running it, instance name, ip, etc. """
        return

    @abc.abstractmethod
    def get_handles(self):
        """Return list of handles to be processed. """
        return


    @abc.abstractmethod
    def get_next_handle(self):
        """Return handle next in queue to be process etc """
        return


    @abc.abstractmethod
    def report_status(self):
        """Report current progress status of task. """
        return


    @abc.abstractmethod
    def store(self):
        """Action to store the result. """
        return


    @abc.abstractmethod
    def remove_context(self):
        """Perform any clean up work to delete this context. """
        return

