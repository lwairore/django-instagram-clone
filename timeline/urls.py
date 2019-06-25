from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url('^$', views.timeline_page, name='timeline'),
    url('^comment/(\d+)/$', views.comment, name="comment"),
    url(r'^like/(\d+)/$', views.like, name='like'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    