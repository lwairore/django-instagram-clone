from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^suggestions/$', views.index, name='homepage'),
    url(r'^new/image$', views.new_image, name='new-image'),
    # url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    #  url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^follow/(\d+)/$', views.follow, name="follow"),
    url(r'^$', views.home_intro, name="intro" ),
    url(r'^search/', views.search_results, name='search_results')
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)