import abc

class Task_Collect(object):

    @abc.abstractmethod
    def init_context(self, context):

    @abc.abstractmethod
    def get_task_info(self):

    @abc.abstractmethod
    def get_handles(self):

    @abc.abstractmethod
    def get_next_handle(self):

    @abc.abstractmethod
    def report_status(self):

    @abc.abstractmethod
    def store_result(self):

    @abc.abstractmethod
    def remove_context(self):

