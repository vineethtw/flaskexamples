from engine import celery


@celery.app.task
def add(x, y):
    return x + y
