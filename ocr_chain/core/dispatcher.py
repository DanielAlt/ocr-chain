import os, time

from .. import image_process
from . import (
    logger as Logger,
    helpers as Helpers
)

class Dispatcher():

    def __init__(self, tasks, **kwargs):
        self.config = Helpers.updateConfig({
            'maximum_threads': 2,
            'refresh_interval': 40,
            'application': 'Dispatcher',
            'log_level': Logger.DEBUG,
            'environment': Logger.PRODUCTION,
            'log_path': os.getcwd(),
            'output_dir': os.path.join( os.getcwd(), 'output-text' )
        }, kwargs)

        self.logger = Logger.Logger(**kwargs)
        self.logger.log(Logger.INFO, "Dispatcher Initialized")

        self.task_queue = tasks
        self.finished_tasks = []
        self.active_tasks = []

        self.awake = True

    def run(self):
        while (self.awake):
            time.sleep(self.config['refresh_interval']/1000.0)

            """ Start new Tasks """
            threads_to_create = self.config['maximum_threads'] - len(self.active_tasks)
            threads_to_create = threads_to_create if ( threads_to_create <= len(self.task_queue) ) else len(self.task_queue)

            if (threads_to_create > 0):
                for x in range(0, threads_to_create):
                    thread_filename = self.task_queue.pop(0)
                    thread = image_process.ImageProcess(thread_filename, self.config['output_dir'])
                    thread.start()
                    self.active_tasks.append(thread)
                    self.logger.log(Logger.INFO, 'launching task: %s, in task queue' % thread_filename)

            """ Kill old Tasks """
            for thread in self.active_tasks:
                if not thread.isAlive():
                    self.active_tasks.remove(thread)
                    self.finished_tasks.append(thread)
                    self.logger.log(Logger.INFO, 'finished task: %s,' % thread.filepath)

            """ Stop The Loop If We're Done Working """
            if (len(self.task_queue) <= 0) and (len(self.active_tasks) <= 0):
                self.awake = False
