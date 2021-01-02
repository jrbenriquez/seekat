from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.shortcuts import render, redirect, reverse

from django.views.generic import TemplateView, View

from se_core.models.seeker import Seeker
from se_core.forms.signup import UserSignUpForm
from se_core.forms.seeker import SeekerForm

User = get_user_model()


class ProfileView(View):
    template_name = 'frontend_alpha/profile.html'

    def get(self, request, seeker_id, *args, **kwargs):
        if isinstance(seeker_id, int):
            seeker = Seeker.objects.get(id=seeker_id)
        elif isinstance(seeker_id, str) and seeker_id == 'me':
            user = request.user
            if not hasattr(user, 'seeker'):
                return redirect('google.com')
            seeker = user.seeker
        else:
            return redirect('google.com')

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
            user = form.save(commit=True)

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





