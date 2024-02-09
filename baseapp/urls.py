from django.urls import path
from .views   import FeedbackListCreateAPIView,FeedbackDetailAPIView
urlpatterns = [
    
    path('feedbacks/', FeedbackListCreateAPIView.as_view(), name='feedback-list-create'),
    path('feedbacks/<int:pk>/', FeedbackDetailAPIView.as_view(), name='feedback-detail'),

]
