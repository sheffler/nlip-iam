# A simple middleware to log requests.
# 
# https://docs.djangoproject.com/en/3.0/topics/http/middleware/#writing-your-own-middleware
# https://docs.djangoproject.com/en/5.1/howto/logging/


import logging

class LogHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger('my_logger')

    def __call__(self, request):
        self.logger.info(f"Request headers: {request.headers}")
        print(f"Request: {request}")
        print(f"Request headers: {request.headers}")
        response = self.get_response(request)
        print(f"Response: {response}")
        print(f"Response headers: {response.headers}")
        print(f"Response content: {response.content}")
        return response
