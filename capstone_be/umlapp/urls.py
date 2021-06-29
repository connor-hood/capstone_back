from django.urls import path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('', RedirectView.as_view(url='/users')),
    path('songs/', views.SongList.as_view()),
    path('songs/<int:pk>/', views.SongDetail.as_view()),
    path('playlists/', views.PlaylistList.as_view()),
    path('playlists/<int:pk>/', views.PlaylistDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/<int:pk>/playlists/<int:fk>/', views.UserPlaylistDetail.as_view()),
    path('users/<int:pk>/playlists/', views.UserPlaylistList.as_view()),
    path('users/<int:pk>/favorites/', views.UserFavoriteList.as_view())
]
