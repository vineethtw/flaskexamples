'''
Sample Celery Abstraction Module
'''
from __future__ import absolute_import

from celery import Celery
from subprocess import Popen

app = Celery('engine',
                broker='sqla+sqlite:///foo.db',
                backend='database',
                include=['engine.tasks', 'waiting_on_tasks.tasks'])

app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERY_RESULT_DBURI="sqlite:///foo.db",
    CELERY_DISABLE_RATE_LIMITS=True,
    CELERY_ACCEPT_CONTENT=['pickle', 'json', 'msgpack', 'yaml']
)


class CeleryEngine:
    def __init__(self):
        pass

    def __enter__(self):
        self.pid = Popen(['celery', 'worker', '--app=engine','--loglevel=INFO', '-q'])
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.pid.terminate()
        return True
