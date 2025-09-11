from django.shortcuts import render, redirect
from django.views.generic import View, FormView, CreateView, ListView, TemplateView
from .forms import ContactUs, ContactUsModelForm
from .models import ContactUs, UserProfile
from django.urls import reverse
from site_module.models import SiteSettings


from django.urls import reverse_lazy

from django.contrib import messages
from django.urls import reverse_lazy

class ContactUsView(CreateView):
    form_class = ContactUsModelForm
    template_name = 'contact_module/contactus_page.html'
    success_url = reverse_lazy('contact_page_urls')

    def form_valid(self, form):
        messages.success(self.request, '✅ پیام شما با موفقیت ارسال شد. کارشناسان ما به زودی با شما تماس خواهند گرفت.')
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        setting: SiteSettings = SiteSettings.objects.filter(is_main_settings=True).first()
        context['site_settings'] = setting
        return context




def store_file(file):
    with open('temp/image.jpg', "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile_page.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/contact-us/register'


class ProfilesView(ListView):
    template_name = 'contact_module/profiles_list_page.html'
    model = UserProfile
    fields = '__all__'
    context_object_name = 'profiles'
    success_url = '/contact-us/profiles_view'
