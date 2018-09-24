from django.contrib import admin
from django import forms
from .models import Document, ClientAnswer, DocumentInfo, DocumentType

class DocumentAdminForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = '__all__'


class DocumentAdmin(admin.ModelAdmin):
    form = DocumentAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated']
    readonly_fields = ['name', 'slug', 'created', 'last_updated']

admin.site.register(Document, DocumentAdmin)


class ClientAnswerAdminForm(forms.ModelForm):

    class Meta:
        model = ClientAnswer
        fields = '__all__'


class ClientAnswerAdmin(admin.ModelAdmin):
    form = ClientAnswerAdminForm
    list_display = ['answer']
    readonly_fields = ['answer']

admin.site.register(ClientAnswer, ClientAnswerAdmin)


class DocumentInfoAdminForm(forms.ModelForm):

    class Meta:
        model = DocumentInfo
        fields = '__all__'


class DocumentInfoAdmin(admin.ModelAdmin):
    form = DocumentInfoAdminForm
    list_display = ['name', 'question', 'field_type']
    readonly_fields = ['name', 'question', 'field_type']

admin.site.register(DocumentInfo, DocumentInfoAdmin)


class DocumentTypeAdminForm(forms.ModelForm):

    class Meta:
        model = DocumentType
        fields = '__all__'


class DocumentTypeAdmin(admin.ModelAdmin):
    form = DocumentTypeAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'template']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'template']

admin.site.register(DocumentType, DocumentTypeAdmin)


