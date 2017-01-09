
from django.conf.urls import url,include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from main import urls as UrlsMain

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include(UrlsMain,namespace="home")),
    url('social-auth/',include('social.apps.django_app.urls', namespace='social')),
    url(
    	regex=r'^media/(?P<path>.*)$',
    	view=serve,
    	kwargs={'document_root':settings.MEDIA_ROOT}),
]
