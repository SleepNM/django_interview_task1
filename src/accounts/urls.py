from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import create_user_form, home_view, UserListView, UserDetailView


urlpatterns = [
    path("", home_view, name="home"),
    path("register/", create_user_form, name="register"),
    path(
        "login/",
        LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("users/", UserListView.as_view(), name="users"),
    path("users/details/<int:pk>/", UserDetailView.as_view(), name="details"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("hijack/", include("hijack.urls", namespace="hijack")),
]
