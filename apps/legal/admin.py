# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from .models import Document, DocumentInfo, Client, ClientAnswer, DocumentType
from .forms import ClientAnswerForm


class ClientAnswerInline(admin.StackedInline):
    model = ClientAnswer
    form = ClientAnswerForm
    extra = 0
    fields = ["answer",]

class DocumentAdmin(admin.ModelAdmin):
    model = Document
    list_display = ('client', 'type')
    inlines = [ClientAnswerInline]

class DocumentInfoAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = DocumentInfo
    fields = ["name", "question", "field_type", ]



# Register your models here.
admin.site.register(Document, DocumentAdmin)
admin.site.register(ClientAnswer)
admin.site.register(Client)
admin.site.register(DocumentInfo, DocumentInfoAdmin)
admin.site.register(DocumentType)
