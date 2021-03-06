from django.urls import path
from . import views
from .views import SearchResultsView


urlpatterns = [
    path("", views.index, name="index"),
    path('painters/', views.painter_index, name="painters"),
    path('painter<int:pk>/', views.painter_detail, name="painter_detail"),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('paintings/', views.PaintingListView.as_view(), name='paintings'),
    path('painting/<int:pk>/', views.PaintingDetailView.as_view(), name='painting_detail'),
]
