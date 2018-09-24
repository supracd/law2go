from . import models

from rest_framework import serializers


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Document
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
        )


class ClientAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ClientAnswer
        fields = (
            'pk', 
            'answer', 
        )


class DocumentInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DocumentInfo
        fields = (
            'pk', 
            'name', 
            'question', 
            'field_type', 
        )


class DocumentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DocumentType
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'template', 
        )


