from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import Feedback, Movie, TVShow
from .serializers import FeedbackSerializer, MovieSerializer, TVShowSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from .models import Fav
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


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

        print(serializer.validated_data)
        return super().perform_create(serializer)


class MovieDetailView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class TVShowListCreateView(ListCreateAPIView):
    queryset = TVShow.objects.all()
    serializer_class = TVShowSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class TVShowDetailView(RetrieveAPIView):
    queryset = TVShow.objects.all()
    serializer_class = TVShowSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_to_favorites(request):
    user = request.user

    # Extract content type and object ID from request data
    content_type = request.data.get("content_type")
    object_id = request.data.get("object_id")

    # Check if content type and object ID are provided
    if not content_type or not object_id:
        return Response(
            {"error": "Content type and object ID are required."}, status=400
        )

    # Check if the content type is valid
    if content_type not in ["movie", "tvshow"]:
        return Response({"error": "Invalid content type."}, status=400)

    # Retrieve the favorite item based on the content type and object ID
    try:
        favorite, created = Fav.objects.get_or_create(
            user=user, favorite_type=content_type, item_id=object_id
        )
    except ValueError:
        return Response({"error": "Invalid object ID."}, status=400)

    # If the favorite was created, add it to the user's favorites
    if created:
        return Response(
            {"success": f"{content_type.capitalize()} added to favorites."}, status=201
        )
    else:
        return Response(
            {"success": f"{content_type.capitalize()} is already in favorites."},
            status=200,
        )


@api_view(["DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def remove_favorite(request):
    user = request.user
    content_type = request.data.get("content_type")
    object_id = request.data.get("object_id")

    if not content_type or not object_id:
        return Response(
            {"error": "Content type and object ID are required."}, status=400
        )

    try:
        favorite = Fav.objects.get(
            user=user, favorite_type=content_type, item_id=object_id
        )
        favorite.delete()
        return Response(
            {"success": f"{content_type.capitalize()} removed from favorites."}
        )
    except Fav.DoesNotExist:
        return Response(
            {"error": f"{content_type.capitalize()} is not in favorites."}, status=404
        )


@api_view(["GET"])
@login_required
def user_favorites(request):
    if request.method == "GET":
        # Retrieve favorites for the authenticated user
        user_favorites = Fav.objects.filter(user=request.user)
        favorites_data = []

        # Construct data for each favorite item
        for favorite in user_favorites:
            favorite_data = {
                "id": favorite.id,
                "favorite_type": favorite.favorite_type,
                "item_id": favorite.item_id,
            }
            if favorite.favorite_type == "movie":
                movie = get_object_or_404(Movie, id=favorite.item_id)
                favorite_data["name"] = movie.title
            elif favorite.favorite_type == "tvshow":
                tvshow = get_object_or_404(TVShow, id=favorite.item_id)
                favorite_data["name"] = tvshow.title

            favorites_data.append(favorite_data)

        return Response(favorites_data, status=status.HTTP_200_OK)


# view for updating user notification preference


@api_view(["GET", "PUT"])
@permission_classes([IsAuthenticated])
def update_or_get_notification_preference(request):
    user = request.user
    if request.method == "GET":
        return Response({"notifications_enabled": user.notifications_enabled})
    elif request.method == "PUT":
        try:
            notifications_enabled = request.data.get("notifications_enabled", False)
            user.notifications_enabled = notifications_enabled
            user.save()
            return Response({"notifications_enabled": notifications_enabled})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
