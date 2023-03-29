
from django.urls import path
from sabai_app import views
urlpatterns = [
    path(
        "",
        views.HomeView.as_view(),
        name="home"
        ),
]
