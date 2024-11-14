# TOM: 2024-11-11
# https://www.google.com/search?q=django+log+request+headeres&sca_esv=93dba3a330e5cf9e&sxsrf=ADLYWII-3TntQ1EYVlAN8wpEI2RLd1mTCQ%3A1731372257812&source=hp&ei=4aQyZ8G7L_T9kPIPyL-sgAc&iflsig=AL9hbdgAAAAAZzKy8XdkkFDcZXxLhowPi00Zyn3hUPTv&ved=0ahUKEwiBsJijyNWJAxX0PkQIHcgfC3AQ4dUDCBk&uact=5&oq=django+log+request+headeres&gs_lp=Egdnd3Mtd2l6IhtkamFuZ28gbG9nIHJlcXVlc3QgaGVhZGVyZXMyBxAAGIAEGA0yCBAAGIAEGKIEMggQABiABBiiBEjCHlAAWLAdcAB4AJABAJgBgAGgAeYPqgEEMjYuMbgBA8gBAPgBAZgCG6AC4hDCAgQQIxgnwgILEAAYgAQYkQIYigXCAg4QLhiABBixAxiDARiKBcICCxAuGIAEGLEDGIMBwgIOEC4YgAQYsQMY0QMYxwHCAgUQABiABMICChAAGIAEGEMYigXCAgsQABiABBixAxiDAcICDRAAGIAEGLEDGEMYigXCAgoQIxiABBgnGIoFwgIFEC4YgATCAgoQABiABBgUGIcCwgIGEAAYFhgemAMAkgcEMjYuMaAHvMIB&sclient=gws-wiz


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
