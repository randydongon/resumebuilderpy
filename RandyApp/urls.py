from django.conf.urls import url
from RandyApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^typesofresume/$', views.typesofresumeApi),
    url(r'^typesofresume/([0-9]+)$', views.typesofresumeApi),

    url(r'^profile/$', views.profileApi),
    url(r'^profile/([0-9]+)$', views.profileApi),

    url(r'^SaveFile$', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
