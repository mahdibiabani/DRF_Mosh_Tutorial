from django.core.mail import send_mail, mail_admins, EmailMessage, BadHeaderError
from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers
import requests
import logging


'''
using logger in project
'''
# logger = logging.getLogger(__name__)

# class Helloview(APIView):
#     def get(self, request):
#           try:
#                logger.info('calling httpbin')
#                response = requests.get('https://httpbin.org/delay/2')
#                logger.info('recieved the response')
#                data= response.json()
#           except requests.ConnectionError:
#                logger.critical('httpbinis offline')     
#           return render(request, 'hello.html', {'name': 'Mahdi'})

#---------------------------------------------------------------
"""
classbase view
"""
class Helloview(APIView):
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
          response = requests.get('https://httpbin.org/delay/2')
          data= response.json()
          return render(request, 'hello.html', {'name': 'Mahdi'})
                
        
"""
functional view
"""
# @cache_page(5 * 60)
# def say_hello(request):
#         response = requests.get('https://httpbin.org/delay/2')
#         data= response.json()
#         return render(request, 'hello.html', {'name': data})



#---------cache data-----------
# def say_hello(request):
#     key = 'http_result'
#     if cache.get(key) is None:
#         response = requests.get('https://httpbin.org/delay/2')
#         data= response.json()
#         cache.set(key, data)
#     return render(request, 'hello.html', {'name': cache.get(key)})
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
    # """
    #     celery usage
    # """
    # notify_customers.delay('Hello')
    
    # return render(request, 'hello.html', {'name': 'Mosh'})

#-----------------------------------------------------------------
