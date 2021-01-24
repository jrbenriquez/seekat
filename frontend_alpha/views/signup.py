from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
from django.views.generic import View

from se_core.forms.seeker import SeekerForm
from se_core.forms.signup import UserSignUpForm
from se_core.models.seeker import Seeker

User = get_user_model()


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





