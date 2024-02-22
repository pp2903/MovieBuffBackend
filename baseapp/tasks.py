from time import sleep
from celery import shared_task

@shared_task
def printHi():
    sleep(2)
    return "Hello!"
    
@shared_task
def sendFavs():
    return "Favorite mail"