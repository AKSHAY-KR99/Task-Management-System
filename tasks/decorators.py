from functools import wraps
from django.shortcuts import render
from django.http import HttpResponseForbidden

def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return render(request, "403_error.html", status=403)

            if request.user.role not in allowed_roles:
                return render(request, "403_error.html", status=403)

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator


def admin_required(view_func):
    return role_required(["admin"])(view_func)


def super_admin_required(view_func):
    return role_required(["super_admin"])(view_func)


def admin_or_super_admin_required(view_func):
    return role_required(["admin", "super_admin"])(view_func)