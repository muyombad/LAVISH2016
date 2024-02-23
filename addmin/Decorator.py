# decorators.py
from functools import wraps
from django.shortcuts import redirect

def session_required(session_key, redirect_to):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            if session_key in request.session:
                return view_func(request, *args, **kwargs)
            else:
                return redirect(redirect_to)
        return wrapped_view
    return decorator
