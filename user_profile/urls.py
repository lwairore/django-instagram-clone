from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url('^$', views.edit_profile_page, name='edit_profile_page'),
    url('^profile/$', views.new_profile, name='new_profile')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)