

from celery import shared_task
from time import sleep

from django.core.mail import send_mail




@shared_task
def add(duration):
    sleep(duration)
    return None
    

@shared_task
def send_mail_task():
    send_mail("celery on work.." , "this is very useful", 
              
            "makwanagautam199@gmail.com",
            ["gautamsinh987@gmail.com"],
            fail_silently = False
            )
    return None    
    
