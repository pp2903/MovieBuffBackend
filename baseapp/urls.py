from django.urls import path
from .views   import FeedbackListCreateAPIView,FeedbackDetailAPIView
from . import views
urlpatterns = [
    
    path('feedbacks/', FeedbackListCreateAPIView.as_view(), name='feedback-list-create'),
    path('feedbacks/<int:pk>/', FeedbackDetailAPIView.as_view(), name='feedback-detail'),
    path('movies/', views.MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),

]
