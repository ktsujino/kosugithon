from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from one_bit.views import WhiteboardView
from one_bit.views import APIDescriptionView

from django.contrib import admin
import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'one_bit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^get_people', 'one_bit.views.get_people'),
    url(r'^set', 'one_bit.views.set'),
    url(r'^get', 'one_bit.views.get'),
    url(r'^delete', 'one_bit.views.delete'),
    url(r'^view', WhiteboardView.as_view(template_name="whiteboard.html")),
    url(r'^form', WhiteboardView.as_view(template_name="form.html")),
    url(r'^api_description', APIDescriptionView.as_view(template_name="api_description.html")),
    url(r'logo', TemplateView.as_view(template_name='logo.jpg'), name='about'),
)
