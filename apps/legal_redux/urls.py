from django.conf.urls import url, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'document', api.DocumentViewSet)
router.register(r'clientanswer', api.ClientAnswerViewSet)
router.register(r'documentinfo', api.DocumentInfoViewSet)
router.register(r'documenttype', api.DocumentTypeViewSet)


urlpatterns = [
    # urls for Django Rest Framework API
    url('api/v1/', include(router.urls)),
]

urlpatterns += [
    # urls for Document
    url('legal_redux/document/', views.DocumentListView.as_view(), name='legal_redux_document_list'),
    url('legal_redux/document/create/', views.DocumentCreateView.as_view(), name='legal_redux_document_create'),
    url('legal_redux/document/detail/<slug:slug>/', views.DocumentDetailView.as_view(), name='legal_redux_document_detail'),
    url('legal_redux/document/update/<slug:slug>/', views.DocumentUpdateView.as_view(), name='legal_redux_document_update'),
]

urlpatterns += [
    # urls for ClientAnswer
    url('legal_redux/clientanswer/', views.ClientAnswerListView.as_view(), name='legal_redux_clientanswer_list'),
    url('legal_redux/clientanswer/create/', views.ClientAnswerCreateView.as_view(), name='legal_redux_clientanswer_create'),
    url('legal_redux/clientanswer/detail/<int:pk>/', views.ClientAnswerDetailView.as_view(), name='legal_redux_clientanswer_detail'),
    url('legal_redux/clientanswer/update/<int:pk>/', views.ClientAnswerUpdateView.as_view(), name='legal_redux_clientanswer_update'),
]

urlpatterns += [
    # urls for DocumentInfo
    url('legal_redux/documentinfo/', views.DocumentInfoListView.as_view(), name='legal_redux_documentinfo_list'),
    url('legal_redux/documentinfo/create/', views.DocumentInfoCreateView.as_view(), name='legal_redux_documentinfo_create'),
    url('legal_redux/documentinfo/detail/<int:pk>/', views.DocumentInfoDetailView.as_view(), name='legal_redux_documentinfo_detail'),
    url('legal_redux/documentinfo/update/<int:pk>/', views.DocumentInfoUpdateView.as_view(), name='legal_redux_documentinfo_update'),
]

urlpatterns += [
    # urls for DocumentType
    url('legal_redux/documenttype/', views.DocumentTypeListView.as_view(), name='legal_redux_documenttype_list'),
    url('legal_redux/documenttype/create/', views.DocumentTypeCreateView.as_view(), name='legal_redux_documenttype_create'),
    url('legal_redux/documenttype/detail/<slug:slug>/', views.DocumentTypeDetailView.as_view(), name='legal_redux_documenttype_detail'),
    url('legal_redux/documenttype/update/<slug:slug>/', views.DocumentTypeUpdateView.as_view(), name='legal_redux_documenttype_update'),
]
