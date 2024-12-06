from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect



class LoginRequiredPermissionMixin(LoginRequiredMixin):
    """Міксин для перевірки, що користувач залогінений."""
    login_url = '/login/'

class RedirectAuthenticatedUserMixin(AccessMixin):
    """Міксин для перенаправлення залогінених користувачів."""
    def dispatch(self, request, *args, **kwargs):
        # Перевіряємо, чи користувач автентифікований
        if request.user.is_authenticated:
            return redirect('profile')  # Замініть 'profile' на ім'я URL профілю
        # Якщо користувач не автентифікований, виконуємо стандартний dispatch
        return super().dispatch(request, *args, **kwargs)