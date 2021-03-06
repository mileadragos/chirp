from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView

from message.views import RegisterView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
]
