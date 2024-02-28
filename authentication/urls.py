from django.urls import path
from .views import AppUserListCreateAPIView, AppUserDetailUpdateDeleteView
from . import views

urlpatterns = [
    path("login/", views.user_login, name="user_login"),
    path("signup/", views.sign_up, name="sign_up"),
    path("users/", AppUserListCreateAPIView.as_view(), name="user-list-create"),
    path(
        "users/<int:pk>",
        AppUserDetailUpdateDeleteView.as_view(),
        name="user-detail-update-delete",
    ),
]
