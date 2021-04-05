from django.urls import path
from . import views
app_name = "account"
urlpatterns = [
    path('home/',views.home_view, name='home'),
    path("register/", views.register_view, name = "register"),
    path("login/", views.logins_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]