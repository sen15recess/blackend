from django.conf import settings
from django.conf.urls import  include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

from account.views import LogoutView


urlpatterns = [
    url(r"^account/$", TemplateView.as_view(template_name="social_homepage.html"), name="home"),
    url(r"^account/social/", include("social.apps.django_app.urls", namespace="social")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
