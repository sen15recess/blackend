from django.conf import settings 
from django.conf.urls import url,include,static
from django.views.generic import TemplateView


urlpatterns = [
	url(r"^account/", include("account.urls")),
	# url(r"", include("authsocial.urls")),
    url(r"^$", TemplateView.as_view(template_name="_homepage.html"), name="home"),
]

if settings.DEBUG:
	urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)