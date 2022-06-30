

from django.core.mail import send_mail

def send_mail_with_out_celery():
    send_mail("celery on work.." , "this is very useful", 
              
            "makwanagautam199@gmail.com",
            ["gautamsinh987@gmail.com"],
            fail_silently = False
            )
    return None    