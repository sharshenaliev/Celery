from celery import shared_task
from datetime import datetime


@shared_task
def test():
    time = datetime.now()
    print(time)


@shared_task
def test_task():
    print('test')


@shared_task
def get_price():
    print('price')
