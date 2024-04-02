# middleware.py

from django.contrib.auth import logout
from django.core.signals import request_finished
from django.dispatch import receiver
from django.utils.deprecation import MiddlewareMixin


class ShutdownListenerMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__(get_response)
        self.server_shutting_down = False

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_request(self, request):
        pass

    def process_response(self, request, response):
        return response

    def process_exception(self, request, exception):
        pass

    def shutdown_listener(self, sender, **kwargs):
        self.server_shutting_down = True

    def check_server_shutdown(self):
        return self.server_shutting_down

# Signal receiver to log out users when a request is finished
@receiver(request_finished)
def logout_on_shutdown(sender, **kwargs):
    shutdown_middleware = ShutdownListenerMiddleware()
    if shutdown_middleware.check_server_shutdown():
        for user in sender._get_user_sessions():
            logout(sender)
