from django import forms
from .models import Document, ClientAnswer, DocumentInfo, DocumentType


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'client', 'type']


class ClientAnswerForm(forms.ModelForm):
    class Meta:
        model = ClientAnswer
        fields = ['answer', 'client', 'document_info', 'document']


class DocumentInfoForm(forms.ModelForm):
    class Meta:
        model = DocumentInfo
        fields = ['name', 'question', 'field_type']


class DocumentTypeForm(forms.ModelForm):
    class Meta:
        model = DocumentType
        fields = ['name', 'template']


