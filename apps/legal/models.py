from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from sitetree.models import Tree as SiteTree
from django.forms import ModelForm
from filebrowser.fields import FileBrowseField
from PyPDF2 import PdfFileWriter, PdfFileReader
import re, uuid
from django.contrib.auth.models import User
from datetime import datetime
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject
class DocumentType(models.Model):

    name = models.CharField(max_length=100, unique=True, help_text='Display name for document')
    description = models.TextField(blank=True, null=True)
    template = FileBrowseField(max_length=200,
                                   blank=True,
                                   directory=settings.LEGAL_TEMPLATE_DIR,
                                   format='document',
                                   help_text='PDF Templates')

    def __unicode__(self):
        return self.name

class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.ForeignKey(DocumentType, blank=True, null=True)
    client = models.ForeignKey(User)


    def get_absolute_url(self):
        return reverse('document_detail', args=(self.id,))

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


    def set_need_appearances_writer(self, writer):
        # See 12.7.2 and 7.7.2 for more information: http://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf
        try:
            catalog = writer._root_object
            # get the AcroForm tree
            if "/AcroForm" not in catalog:
                writer._root_object.update({
                    NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)})

            need_appearances = NameObject("/NeedAppearances")
            writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
            return writer

        except Exception as e:
            print('set_need_appearances_writer() catch : ', repr(e))
            return writer

    def generate_document(self):
        pdf = PdfFileReader(self.type.template.path_full)
        pdf_out = PdfFileWriter()
        pdf_out = self.set_need_appearances_writer(pdf_out)
        for page in range(pdf.getNumPages()):
            pdf_out.addPage(pdf.getPage(page))
            values = {}
            for answer in ClientAnswer.objects.filter(document=self, client=self.client):
                values[answer.document_info.name] = answer.answer
                #This is terrible
                for _ in range(1, 20):

                    values['{}_{}'.format(str(answer.document_info.name), str(_))] = answer.answer
                if answer.document_info.field_type == 'date':
                    try:
                        date = datetime.strptime(answer.answer, '%Y-%m-%d')
                        values['|'.join([answer.document_info.name, 'day'])] = date.day
                        values['|'.join([answer.document_info.name, 'month'])] = date.strftime("%B")
                        values['|'.join([answer.document_info.name, 'year'])] = date.year
                        values['|'.join([answer.document_info.name, 'year', '2'])] = str(date.year)[2:]
                    except ValueError as e:
                        pass

            pdf_out.updatePageFormFieldValues(pdf_out.getPage(page), values)
        return pdf_out


    def __unicode__(self):
        return '{} {}'.format(self.type.name, self.client)



class Client(models.Model):
    name = models.CharField(max_length=500, help_text='Client Name')

    def __unicode__(self):
        return self.name

class ClientAnswer(models.Model):
    answer = models.TextField(null=True, blank=True)
    client = models.ForeignKey(User, null=True, blank=True)
    document_info = models.ForeignKey('DocumentInfo', null=True, blank=True)
    document = models.ForeignKey('Document', null=True, blank=True)

    def __unicode__(self):
        return '{} {} - {}'.format(self.client.first_name, self.client.last_name, self.document_info.name)

    class Meta:
        ordering = ['document_info__display_order',]

class DocumentInfo(models.Model):
    FIELD_TYPE_CHOICES = (
      ('text', 'Name'),
      ('date', 'Date'),
      ('text', 'Short Text'),
      ('textarea', 'Long Text'),

    )
    name = models.CharField(max_length=100, unique=True, help_text='Unique Name/ID for a document info.')
    question = models.TextField(blank=True, null=True)
    field_type = models.CharField(max_length=100, default='name', choices=FIELD_TYPE_CHOICES)
    display_order = models.IntegerField(default=0)


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['display_order',]
