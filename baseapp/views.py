from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import Feedback,Movie,TVShow
from .serializers import FeedbackSerializer,MovieSerializer,TVShowSerializer
from django.db import models
from authentication.models import AppUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import  status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.contenttypes.models import ContentType
from .models import Fav


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
    


    
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_to_favorites(request):
    user = request.user
    
    # Extract content type and object ID from request data
    content_type = request.data.get('content_type')
    object_id = request.data.get('object_id')
    
    # Check if content type and object ID are provided
    if not content_type or not object_id:
        return Response({'error': 'Content type and object ID are required.'}, status=400)
    
    # Check if the content type is valid
    if content_type not in ['movie', 'tvshow']:
        return Response({'error': 'Invalid content type.'}, status=400)
    
    # Retrieve the favorite item based on the content type and object ID
    try:
        favorite, created = Fav.objects.get_or_create(user=user, favorite_type=content_type, item_id=object_id)
    except ValueError:
        return Response({'error': 'Invalid object ID.'}, status=400)

    # If the favorite was created, add it to the user's favorites
    if created:
        return Response({'success': f'{content_type.capitalize()} added to favorites.'}, status=201)
    else:
        return Response({'success': f'{content_type.capitalize()} is already in favorites.'}, status=200)




@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def remove_favorite(request):
    user = request.user
    content_type = request.data.get('content_type')
    object_id = request.data.get('object_id')

    if not content_type or not object_id:
        return Response({'error': 'Content type and object ID are required.'}, status=400)

    try:
        favorite = Fav.objects.get(user=user, favorite_type=content_type, item_id=object_id)
        favorite.delete()
        return Response({'success': f'{content_type.capitalize()} removed from favorites.'})
    except Fav.DoesNotExist:
        return Response({'error': f'{content_type.capitalize()} is not in favorites.'}, status=404)