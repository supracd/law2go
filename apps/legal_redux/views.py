from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Document, ClientAnswer, DocumentInfo, DocumentType
from .forms import DocumentForm, ClientAnswerForm, DocumentInfoForm, DocumentTypeForm


class DocumentListView(ListView):
    model = Document


class DocumentCreateView(CreateView):
    model = Document
    form_class = DocumentForm


class DocumentDetailView(DetailView):
    model = Document


class DocumentUpdateView(UpdateView):
    model = Document
    form_class = DocumentForm


class ClientAnswerListView(ListView):
    model = ClientAnswer


class ClientAnswerCreateView(CreateView):
    model = ClientAnswer
    form_class = ClientAnswerForm


class ClientAnswerDetailView(DetailView):
    model = ClientAnswer


class ClientAnswerUpdateView(UpdateView):
    model = ClientAnswer
    form_class = ClientAnswerForm


class DocumentInfoListView(ListView):
    model = DocumentInfo


class DocumentInfoCreateView(CreateView):
    model = DocumentInfo
    form_class = DocumentInfoForm


class DocumentInfoDetailView(DetailView):
    model = DocumentInfo


class DocumentInfoUpdateView(UpdateView):
    model = DocumentInfo
    form_class = DocumentInfoForm


class DocumentTypeListView(ListView):
    model = DocumentType


class DocumentTypeCreateView(CreateView):
    model = DocumentType
    form_class = DocumentTypeForm


class DocumentTypeDetailView(DetailView):
    model = DocumentType


class DocumentTypeUpdateView(UpdateView):
    model = DocumentType
    form_class = DocumentTypeForm

