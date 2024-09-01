import threading
from functools import wraps
from django.http import JsonResponse
from rest_framework.exceptions import APIException


class TimeoutException(APIException):
    status_code = 504
    default_detail = 'Request timed out'

def timeout_decorator(seconds):
    """
        пришлось написать собственный декоратор для таймаута
        так как готовые решения как django-timeout несовместимы с 
        используемой версией python
    """
    def decorator(func):
        def _wrapper(request, *args, **kwargs):
            result = [None]
            exception = [None]

            def target():
                try:
                    result[0] = func(request, *args, **kwargs)
                except Exception as e:
                    exception[0] = e

            thread = threading.Thread(target=target)
            thread.start()
            thread.join(timeout=seconds)

            if thread.is_alive():
                thread.join(0)  # Finish the thread if still running
                raise TimeoutException()

            if exception[0] is not None:
                raise exception[0]

            return result[0]

        return wraps(func)(_wrapper)
    return decorator