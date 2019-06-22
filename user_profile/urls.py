from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url('^edit/$', views.edit_profile_page, name='edit_profile_page'),
    url('^$', views.profile_page, name='profile_page')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)