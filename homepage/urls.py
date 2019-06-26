from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^suggestions/$', views.index, name='homepage'),
    url(r'^new/image$', views.new_image, name='new-image'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^follow/(\d+)/$', views.follow, name="follow"),
    url(r'^$', views.home_intro, name="intro" ),
    url(r'^search/', views.search_results, name='search_results')
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)