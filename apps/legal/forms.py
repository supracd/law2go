from django import forms
from .models import Document, DocumentInfo, ClientAnswer

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['type']

class DocumentInfoForm(forms.ModelForm):
    class Meta:
        model = DocumentInfo
        fields = ['question', 'display_order']

class ClientAnswerForm(forms.ModelForm):
    class Meta:
        model = ClientAnswer
        fields = ['answer',]
