
from rest_framework import generics
from .models import ChangeLog
from .serializers import ChangeLogSerializer


# List and create view for ChangeLog
class ChangeLogListCreateView(generics.ListCreateAPIView):
    queryset = ChangeLog.objects.all()
    serializer_class = ChangeLogSerializer

# Create-only view for ChangeLog (POST)
class ChangeLogCreateView(generics.CreateAPIView):
    queryset = ChangeLog.objects.all()
    serializer_class = ChangeLogSerializer

# Create your views here.
