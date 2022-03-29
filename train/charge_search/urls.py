from django.urls import path
from . import views


app_name = "charge_search"
urlpatterns = [
    path("", views.top_page, name="top_page"),
    path("joban/", views.joban, name="joban"),
]
