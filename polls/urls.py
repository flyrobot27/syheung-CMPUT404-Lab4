from django.urls import path
from . import views

urlpatterns = [
    # /polls/
    path('', views.IndexView.as_view(), name='index'),
    # /polls/(question_id: int)/
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    # /polls/(question_id: int)/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name="results"),
    # /polls/(question_id: int)/vote/
    path('<int:question_id>/vote/', views.vote, name="vote")
]