from django.urls import path
from django.views.generic import RedirectView

from .views import URLRedirectCreateView, URLRedirectDeleteView, URLRedirectListView, URLRedirectGoToOriginalURLView

appname = "shortener"

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="url-redirect-create")),
    path("create-new-short-URL", URLRedirectCreateView.as_view(), name="url-redirect-create"),
    path("delete-short-URL/<int:pk>", URLRedirectDeleteView.as_view(), name="url-redirect-delete"),
    path("view-created-short-URLs", URLRedirectListView.as_view(), name="url-redirect-list"),
    path("<str:short_URL_suffix>/", URLRedirectGoToOriginalURLView.as_view()),
]