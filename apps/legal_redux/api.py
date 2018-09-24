from . import models
from . import serializers
from rest_framework import viewsets, permissions


class DocumentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Document class"""

    queryset = models.Document.objects.all()
    serializer_class = serializers.DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClientAnswerViewSet(viewsets.ModelViewSet):
    """ViewSet for the ClientAnswer class"""

    queryset = models.ClientAnswer.objects.all()
    serializer_class = serializers.ClientAnswerSerializer
    permission_classes = [permissions.IsAuthenticated]


class DocumentInfoViewSet(viewsets.ModelViewSet):
    """ViewSet for the DocumentInfo class"""

    queryset = models.DocumentInfo.objects.all()
    serializer_class = serializers.DocumentInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class DocumentTypeViewSet(viewsets.ModelViewSet):
    """ViewSet for the DocumentType class"""

    queryset = models.DocumentType.objects.all()
    serializer_class = serializers.DocumentTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


