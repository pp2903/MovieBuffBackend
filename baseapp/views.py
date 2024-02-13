from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import Feedback,Movie,TVShow
from .serializers import FeedbackSerializer,MovieSerializer,TVShowSerializer
from django.db import models
from authentication.models import AppUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import  status



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
    
    def perform_create(self, serializer):
        
        id = self.request.data['id']
        print(serializer.validated_data)
        return super().perform_create(serializer)
    
    
class MovieDetailView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class =MovieSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    
    
    
class TVShowListCreateView(ListCreateAPIView):
    queryset = TVShow.objects.all()
    serializer_class = TVShowSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
class TVShowDetailView(RetrieveAPIView):
    queryset = TVShow.objects.all()
    serializer_class =TVShowSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    