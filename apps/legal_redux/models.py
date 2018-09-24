from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from filebrowser.fields import FileBrowseField
from PyPDF2 import PdfFileWriter, PdfFileReader
from django.contrib.auth.models import User
import re

class Document(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey('DocumentType', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('legal_redux_document_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('legal_redux_document_update', args=(self.slug,))

    def save(self, *args, **kwargs):
        super(Document, self).save(*args, **kwargs)
        pdf = PdfFileReader(self.type.template.path_full)
        for field in pdf.getFormTextFields().keys():
            m = re.search(r'^(.*?)_(\d)$', field)
            if m:
                field = m.groups()[0]
            if '|' in field:
                field = field.split('|')[0]
            document_info = DocumentInfo.objects.get_or_create(name=field)[0]
            document_info.save()
            client_answer = ClientAnswer.objects.get_or_create(document=self, client=self.client, document_info=document_info)[0]
            client_answer.save()
        # Save the Document

    def generate_document(self):
        pdf = PdfFileReader(self.template.path_full)
        pdf_out = PdfFileWriter()
        for page in range(pdf.getNumPages()):
            pdf_out.addPage(pdf.getPage(page))
            values = {}
            for answer in ClientAnswer.objects.filter(document=self, client=self.client):
                values[answer.document_info.name] = answer.answer
                for _ in range(1, 6):

                    values['{}_{}'.format(str(answer.document_info.name), str(_))] = answer.answer

            pdf_out.updatePageFormFieldValues(pdf_out.getPage(page), values)
        return pdf_out

class ClientAnswer(models.Model):

    # Fields
    answer = TextField(null=True, blank=True)

    # Relationship Fields
    client = ForeignKey(
    User,
        null=True, blank=True, on_delete=models.CASCADE
    )
    document_info = ForeignKey(
    'DocumentInfo',
        null=True, blank=True, on_delete=models.CASCADE
    )
    document = ForeignKey(
    Document,
        null=True, blank=True, on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('legal_redux_clientanswer_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('legal_redux_clientanswer_update', args=(self.pk,))


class DocumentInfo(models.Model):
    FIELD_TYPE_CHOICES = (
      ('text', 'Name'),
      ('date', 'Date'),
      ('text', 'Short Text'),
      ('textarea', 'Long Text'),

    )
    # Fields
    name = CharField(max_length=100, unique=True, help_text='Unique Name/ID for a document info.')
    question = TextField(blank=True, null=True)
    field_type = CharField(max_length=100, default='name', choices=FIELD_TYPE_CHOICES)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('legal_redux_documentinfo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('legal_redux_documentinfo_update', args=(self.pk,))


class DocumentType(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    template = FileBrowseField(max_length=200,
                                   blank=True,
                                   directory=settings.LEGAL_TEMPLATE_DIR,
                                   format='document',
                                   help_text='PDF Templates')


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('legal_redux_documenttype_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('legal_redux_documenttype_update', args=(self.slug,))
