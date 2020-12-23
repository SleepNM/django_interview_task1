from django.urls import path
from .views import create_user_form, home_view


urlpatterns = [
    path("", home_view, name="home"),
    path("register/", create_user_form, name="register"),
]
