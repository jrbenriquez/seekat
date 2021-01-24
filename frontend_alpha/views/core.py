from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect, reverse
from django.views.generic import View

from se_core.forms.seeker import SeekerForm
from se_core.forms.signup import UserSignUpForm
from se_core.models.seeker import Seeker

User = get_user_model()

class LogoutView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('frontend_alpha:login'))


class LoginView(View):
    template_name = 'frontend_alpha/login.html'

    def get(self, request, *args, **kwargs):
        next_url = request.GET.get('next', None)

        user = request.user
        if user.is_authenticated and hasattr(user, 'seeker'):
            return redirect(
                reverse('frontend:profile', kwargs={'seeker_id': 'me'}))
        context = {
            "next_url": next_url
        }

        return render(
            request,
            self.template_name,
            context=context)

    def post(self, request, *args, **kwargs):
        next_url = request.POST.get('next', None)
        username_email = request.POST.get('username_email', None)
        password = request.POST.get('password', None)

        def return_error(errors):
            context = {
                "username_email": username_email,
                "errors": errors,
                "next_url": next_url,
            }

            return render(
                request,
                self.template_name,
                context=context)

        errors = {}
        if not username_email:
            errors['username_email'] = ['Username / Email is required', ]
        if not password:
            errors['Password'] = ['Password is required', ]

        q_username = Q(username=username_email)
        q_email = Q(email=username_email)

        user_query = User.objects.filter(q_username | q_email)
        if not user_query.exists():
            errors['Username/Email'] = ['Username/Email does not exist', ]
            return return_error(errors)

        user = user_query.get()
        valid_password = user.check_password(password)
        if not valid_password:
            errors['Password'] = ['Incorrect credentials. Please try again', ]
        if errors:
            return return_error(errors)

        login(request, user)

        if next_url:
            return redirect(next_url)

        return redirect(
            reverse('frontend:profile', kwargs={'seeker_id': 'me'}))


