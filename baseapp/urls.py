from django.urls import path
from .views import FeedbackListCreateAPIView, FeedbackDetailAPIView
from . import views

urlpatterns = [
    path(
        "feedbacks/", FeedbackListCreateAPIView.as_view(), name="feedback-list-create"
    ),
    path(
        "feedbacks/<int:pk>/", FeedbackDetailAPIView.as_view(), name="feedback-detail"
    ),
    path("movies/", views.MovieListCreateView.as_view(), name="movie-list-create"),
    path("movies/<int:pk>/", views.MovieDetailView.as_view(), name="movie-detail"),
    path("tvshows/", views.TVShowListCreateView.as_view(), name="tvshow-list-create"),
    path("tvshows/<int:pk>/", views.TVShowDetailView.as_view(), name="tvshow-detail"),
    path("add_to_favorites/", views.add_to_favorites, name="add_to_favorites"),
    path("remove_favorite/", views.remove_favorite, name="remove_favorite"),
    path("favorites/", views.user_favorites, name="user_favorites"),
    path(
        "user/notification/",
        views.update_or_get_notification_preference,
        name="update_or_get_notification_preference",
    ),
]
