from django.urls import path
from . import views
app_name = "quiz"
urlpatterns = [
    path("python/", views.python_view, name='python'),
    path("java/", views.java_view, name='java'),
    path("c/", views.c_view, name='c'),
    path("score/<int:pk>/", views.score_view, name="score"),


]