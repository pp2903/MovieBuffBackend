from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import Feedback
from .serializers import FeedbackSerializer
from django.db import models
from authentication.models import AppUser

class FeedbackListCreateAPIView(ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    authentication_classes = []
    permission_classes = []

class FeedbackDetailAPIView(RetrieveAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer



