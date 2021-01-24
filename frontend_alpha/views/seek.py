#https://www.w3schools.com/howto/howto_js_filter_lists.asp

from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.views.generic import View

from se_core.models import Seek
from se_core.models import Seekat, Category
from se_core.models import SeekatAddress
from se_core.forms.seek import NewSeekForm
from se_core.forms.seek import AdditionalSeekDetailsForm

User = get_user_model()


class NewSeekView(LoginRequiredMixin, View):
    template_name = 'frontend_alpha/seek/new_seek.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        form = NewSeekForm(request.POST)
        context = {}
        if form.is_valid():
            data = form.cleaned_data
            context["seekat_id"] = data.get('seekat_id')
            context['seekat_name'] = data.get('seekat_name')

            context["category_id"] = data.get('category_id')
            context['category_name'] = data.get('category_name')
            return render(
                request, 'frontend_alpha/seek/new_seek_details.html', context)

        context["form"] = form
        return render(request, self.template_name, context)


class AdditionalSeekDetails(LoginRequiredMixin, View):
    template_name = 'frontend_alpha/seek/new_seek_details.html'

    def post(self, request, *args, **kwargs):
        form = AdditionalSeekDetailsForm(request.POST)
        data = request.POST
        context = {}
        context["seekat_id"] = data.get('seekat_id')
        context['seekat_name'] = data.get('seekat_name')
        context["category_id"] = data.get('category_id')
        context['category_name'] = data.get('category_name')
        if form.is_valid():
            data = form.cleaned_data
            # Update Seekat
            seekat_id = data.get('seekat_id')
            seekat_name = data.get('seekat_name')
            if seekat_id:
                seekat = Seekat.objects.get(id=seekat_id)
            else:
                seekat = Seekat.objects.create(name=seekat_name)

            seekat.parent_id = data.get('seekat_parent_id')
            seekat.description = data.get('seekat_description')
            seekat_line1 = data.get('seekat_line1')
            seekat_line2 = data.get('seekat_line2')
            seekat_zip_code = data.get('seekat_zip_code')
            seekat_city = data.get('seekat_city')
            seekat_state = data.get('seekat_state')
            seekat_country = data.get('seekat_country')
            if any([
                seekat_line1, seekat_line2, seekat_zip_code,
                    seekat_city, seekat_state, seekat_country]):

                if seekat.address:
                    address = seekat.address
                else:
                    address = SeekatAddress.objects.create(
                        name="Default",
                    )
                    seekat.address = address
                    seekat.save(update_fields=['address'])

                if seekat_line1:
                    address.line1 = seekat_line1
                if seekat_line2:
                    address.line2 = seekat_line2
                if seekat_zip_code:
                    address.zip_code = seekat_zip_code
                if seekat_city:
                    address.city = seekat_city
                if seekat_state:
                    address.state = seekat_state
                if seekat_country:
                    address.country = seekat_country

                address.save()
            seekat.save()

            # Update Category
            category_id = data.get('category_id')
            category_name = data.get('category_name')
            if category_id:
                category = Category.objects.get(id=category_id)
            else:
                print(category_name)
                category = Category.objects.create(name=category_name)

            category_parent_id = data.get('category_parent_id')

            if category_parent_id:
                category.parent_id = category_parent_id
            category.save()
            # Create hashtags
            # Create Seek
            Seek.objects.create(
                seeker=request.user.seeker,
                category=category,
                seekat=seekat,
            )

            return redirect(
                reverse('frontend:profile', kwargs={'seeker_id': 'me'}))

        context["form"] = form
        return render(request, self.template_name, context)
