from django.urls import path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('', RedirectView.as_view(url='/songs')),
    path('songs/', views.SongList.as_view()),
    path('songs/<int:pk>/', views.SongDetail.as_view()),
    path('playlists/', views.PlaylistList.as_view()),

]
