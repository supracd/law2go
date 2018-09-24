from django.conf.urls import url
from .views import page_detail

urlpatterns = [
    url(r'^(?P<relative_url>(.*))/$', page_detail, name='pages_page_detail')
]
