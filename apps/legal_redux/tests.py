import unittest
from django.urls import reverse
from django.test import Client
from .models import Document, ClientAnswer, DocumentInfo, DocumentType
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_document(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "client" not in defaults:
        defaults["client"] = create_django_contrib_auth_models_user()
    if "type" not in defaults:
        defaults["type"] = create_documenttype()
    return Document.objects.create(**defaults)


def create_clientanswer(**kwargs):
    defaults = {}
    defaults["answer"] = "answer"
    defaults.update(**kwargs)
    if "client" not in defaults:
        defaults["client"] = create_user()
    if "document_info" not in defaults:
        defaults["document_info"] = create_'documentinfo'()
    if "document" not in defaults:
        defaults["document"] = create_'document'()
    return ClientAnswer.objects.create(**defaults)


def create_documentinfo(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["question"] = "question"
    defaults["field_type"] = "field_type"
    defaults.update(**kwargs)
    return DocumentInfo.objects.create(**defaults)


def create_documenttype(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["template"] = "template"
    defaults.update(**kwargs)
    return DocumentType.objects.create(**defaults)


class DocumentViewTest(unittest.TestCase):
    '''
    Tests for Document
    '''
    def setUp(self):
        self.client = Client()

    def test_list_document(self):
        url = reverse('legal_redux_document_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_document(self):
        url = reverse('legal_redux_document_create')
        data = {
            "name": "name",
            "client": create_django_contrib_auth_models_user().pk,
            "type": create_documenttype().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_document(self):
        document = create_document()
        url = reverse('legal_redux_document_detail', args=[document.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_document(self):
        document = create_document()
        data = {
            "name": "name",
            "client": create_django_contrib_auth_models_user().pk,
            "type": create_documenttype().pk,
        }
        url = reverse('legal_redux_document_update', args=[document.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ClientAnswerViewTest(unittest.TestCase):
    '''
    Tests for ClientAnswer
    '''
    def setUp(self):
        self.client = Client()

    def test_list_clientanswer(self):
        url = reverse('legal_redux_clientanswer_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_clientanswer(self):
        url = reverse('legal_redux_clientanswer_create')
        data = {
            "answer": "answer",
            "client": create_user().pk,
            "document_info": create_'documentinfo'().pk,
            "document": create_'document'().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_clientanswer(self):
        clientanswer = create_clientanswer()
        url = reverse('legal_redux_clientanswer_detail', args=[clientanswer.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_clientanswer(self):
        clientanswer = create_clientanswer()
        data = {
            "answer": "answer",
            "client": create_user().pk,
            "document_info": create_'documentinfo'().pk,
            "document": create_'document'().pk,
        }
        url = reverse('legal_redux_clientanswer_update', args=[clientanswer.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class DocumentInfoViewTest(unittest.TestCase):
    '''
    Tests for DocumentInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_documentinfo(self):
        url = reverse('legal_redux_documentinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_documentinfo(self):
        url = reverse('legal_redux_documentinfo_create')
        data = {
            "name": "name",
            "question": "question",
            "field_type": "field_type",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_documentinfo(self):
        documentinfo = create_documentinfo()
        url = reverse('legal_redux_documentinfo_detail', args=[documentinfo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_documentinfo(self):
        documentinfo = create_documentinfo()
        data = {
            "name": "name",
            "question": "question",
            "field_type": "field_type",
        }
        url = reverse('legal_redux_documentinfo_update', args=[documentinfo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class DocumentTypeViewTest(unittest.TestCase):
    '''
    Tests for DocumentType
    '''
    def setUp(self):
        self.client = Client()

    def test_list_documenttype(self):
        url = reverse('legal_redux_documenttype_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_documenttype(self):
        url = reverse('legal_redux_documenttype_create')
        data = {
            "name": "name",
            "template": "template",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_documenttype(self):
        documenttype = create_documenttype()
        url = reverse('legal_redux_documenttype_detail', args=[documenttype.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_documenttype(self):
        documenttype = create_documenttype()
        data = {
            "name": "name",
            "template": "template",
        }
        url = reverse('legal_redux_documenttype_update', args=[documenttype.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


