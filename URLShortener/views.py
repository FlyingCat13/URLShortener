from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views import View

from .models import URLRedirect

class URLRedirectCreateView(LoginRequiredMixin, CreateView):
    model = URLRedirect
    template_name = "url_redirect_create.html"
    fields = ['original_URL']

    def form_valid(self, form) -> HttpResponse:
        form.instance.created_by = self.request.user
        form.instance.save()

        context = self.get_context_data(form=form)
        context["original_URL"] = form.instance.original_URL
        context["short_URL"] = self.request.build_absolute_uri("/") + form.instance.short_URL_suffix

        return self.render_to_response(context)

class URLRedirectListView(LoginRequiredMixin, ListView):
    template_name = "url_redirect_list.html"

    def get_queryset(self):
        return URLRedirect.objects.filter(created_by=self.request.user)

class URLRedirectDeleteView(LoginRequiredMixin, DeleteView):
    model = URLRedirect
    
    def get_success_url(self):
        return reverse("url-redirect-list")

class URLRedirectGoToOriginalURLView(View):
    def get(self, request, *args, **kwargs) -> HttpResponse:
        try:
            url_redirect = get_object_or_404(URLRedirect, short_URL_suffix=kwargs['short_URL_suffix'])
            url_redirect.access_count += 1
            url_redirect.save()

            return redirect(url_redirect.original_URL, permanent=True)
        except Http404:
            return HttpResponse('<h1>No redirect link at this short URL</h1>')
