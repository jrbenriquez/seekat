from django.shortcuts import render, redirect
from django.views.generic import View

from se_core.models.seeker import Seeker


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
        seeks = seeker.seeks.all()
        context = {
            "seeker": seeker,  # Seeker Profile being viewed
            "seeks": seeks
        }

        return render(
            request,
            self.template_name,
            context=context
        )

