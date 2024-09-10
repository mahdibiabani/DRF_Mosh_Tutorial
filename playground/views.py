from django.core.mail import send_mail, mail_admins, EmailMessage, BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers


def say_hello(request):
#--------------------------------------------------------------=-
    # """sending email"""
    # try:
    #     message = BaseEmailMessage(
    #         template_name='emails/hello.html',
    #         context={'name': 'Mahdi'}
    #     )
    #     message.send(['john@mosh.com'])

    # except BadHeaderError:
    #     pass

#-----------------------------------------------------------------

    notify_customers.delay('Hello')
    
    return render(request, 'hello.html', {'name': 'Mosh'})
