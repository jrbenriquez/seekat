from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import render, redirect, reverse

from django.views.generic import TemplateView, View

from se_core.models.seeker import Seeker
from se_core.forms.signup import UserSignUpForm
from se_core.forms.seeker import SeekerForm

User = get_user_model()

#TODO Add Seek View


class LogoutView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('frontend_alpha:login'))


class LoginView(View):
    template_name = 'frontend_alpha/login.html'

    def get(self, request, *args, **kwargs):
        next_url = request.GET.get('next', None)

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

        errors = {}
        if not username_email:
            errors['username_email'] = ['Username / Email is required', ]
        if not password:
            errors['password'] = ['Password is required', ]

        q_username = Q(username=username_email)
        q_email = Q(email=username_email)

        user_query = User.objects.filter(q_username | q_email)
        if not user_query.exists():
            errors['username_email'] = ['Username/Email does not exist', ]
        user = user_query.get()
        print(user)
        valid_password = user.check_password(password)
        print(password)
        if not valid_password:
            errors['password'] = ['Incorrect credentials. Please try again', ]

        if errors:
            context = {
                "username_email": username_email,
                "errors": errors,
                "next_url": next_url,
            }

            return render(
                request,
                self.template_name,
                context=context)


        login(request, user)

        if next_url:
            return redirect(next_url)

        return redirect(
            reverse('frontend:profile', kwargs={'seeker_id': 'me'}))


class ProfileView(View):
    template_name = 'frontend_alpha/profile.html'

    def get(self, request, seeker_id, *args, **kwargs):
        if isinstance(seeker_id, int):
            seeker = Seeker.objects.get(id=seeker_id)
        elif isinstance(seeker_id, str) and seeker_id == 'me':
            user = request.user
            if not hasattr(user, 'seeker'):
                return redirect('frontend_alpha:login')
            seeker = user.seeker
        else:
            return redirect('frontend_alpha:login')

        context = {
            "seeker": seeker
        }

        return render(
            request,
            self.template_name,
            context=context
        )


class SignUpView(View):
    form_class = UserSignUpForm
    template_name = 'frontend_alpha/signup/signup.html'

    def get(self, request):

        context = {}

        return render(
            request,
            self.template_name,
            context=context
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(form.cleaned_data['password'])
            user.save()

            seeker = Seeker.objects.create(user=user)
            login(request, user)

            return redirect(reverse('frontend:signup-details'))
        context = {
            "form": form,
        }

        return render(
            request,
            self.template_name,
            context=context
        )


class SignUpDetailsView(LoginRequiredMixin, View):
    form_class = SeekerForm
    template_name = 'frontend_alpha/signup/details.html'

    def get(self, request):

        context = {}

        return render(
            request,
            self.template_name,
            context=context
        )

    def post(self, request, *args, **kwargs):

        seeker = request.user.seeker
        form = self.form_class(request.POST, instance=seeker)

        if form.is_valid():
            form.save()
            return redirect(reverse('frontend:profile', kwargs={"seeker_id": "me"}))

        context = {
            "form": form,
        }

        return render(
            request,
            self.template_name,
            context=context
        )





