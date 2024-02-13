from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import Feedback,Movie,TVShow
from .serializers import FeedbackSerializer,MovieSerializer,TVShowSerializer
from django.db import models
from authentication.models import AppUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class FeedbackListCreateAPIView(ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    authentication_classes = []
    permission_classes = []

class FeedbackDetailAPIView(RetrieveAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer



class MovieListCreateView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
class MovieDetailView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class =MovieSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    