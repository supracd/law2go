from django.conf.urls import url
from .views import document_detail, document_listing, DocumentCreateView, DocumentUpdateView

urlpatterns = [
url(r'^create/(?P<type>(.*))/$', DocumentCreateView.as_view(), name='document_create'),

    url(r'^(?P<id>(.*))/$', document_detail, name='document_detail'),

    url(r'^$', document_listing, name='document_listing')
]
