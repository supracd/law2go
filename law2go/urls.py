from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from filebrowser.sites import site

urlpatterns = [
    # Home
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),

    # Blog
    url(r'^blog/', include('blog.urls')),

    # Pages
    url(r'^pages/', include('pages.urls')),

    # Documents
    url(r'^documents/', include('legal.urls')),
    # Filebrowser, DJ Admin, & Grappelli
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),

    # Registration
    url(r'^accounts/', include('registration.backends.simple.urls')),
]

# UPLOAD MEDIA IN DEBUG
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
