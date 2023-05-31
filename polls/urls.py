from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<pk>/", views.PollsDetailView.as_view(),name="detail"),
    path("<pk>/results/", views.ResultsView.as_view(),name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    
]
