from .models import Contact
from .serializers import *
from rest_framework import viewsets

class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer