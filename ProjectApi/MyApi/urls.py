from django.urls import path, include
from .views import (CityViewReverse,
                    AuthorViewReverse,
                    BookViewReverse,
                    CityViewForward,
                    AuthorViewForward,
                    BookViewForward,
                    SongView,
                    SingerView)

from rest_framework.routers import DefaultRouter

city_router_reverse = DefaultRouter(trailing_slash=True)
city_router_reverse.register(r'cities',CityViewReverse,basename='all cities r')

author_router_reverse = DefaultRouter(trailing_slash=True)
author_router_reverse.register(r'authors',AuthorViewReverse,basename='all authors r')

book_router_reverse = DefaultRouter(trailing_slash=True)
book_router_reverse.register(r'books',BookViewReverse,basename='all books r')

city_router_forward = DefaultRouter(trailing_slash=True)
city_router_forward.register(r'cities',CityViewForward,basename='all cities f')

author_router_forward = DefaultRouter(trailing_slash=True)
author_router_forward.register(r'authors',AuthorViewForward,basename='all authors f')

book_router_forward = DefaultRouter(trailing_slash=True)
book_router_forward.register(r'books',BookViewForward,basename='all books f')

song_router = DefaultRouter(trailing_slash=True)
song_router.register(r'songs',SongView,basename='songs')

singer_router = DefaultRouter(trailing_slash=True)
singer_router.register(r'singers',SingerView,basename='singers')

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('city-api/r/',include(city_router_reverse.urls)),
    path('city-api/r/<int:pk>/',include(city_router_reverse.urls)),
    path('author-api/r/',include(author_router_reverse.urls)),
    path('author-api/r/<int:pk>/',include(author_router_reverse.urls)),
    path('book-api/r/',include(book_router_reverse.urls)),
    path('book-api/r/<int:pk>/',include(book_router_reverse.urls)),
    path('city-api/f/', include(city_router_forward.urls)),
    path('city-api/f/<int:pk>/', include(city_router_forward.urls)),
    path('author-api/f/', include(author_router_forward.urls)),
    path('author-api/f/<int:pk>/', include(author_router_forward.urls)),
    path('book-api/f/', include(book_router_forward.urls)),
    path('book-api/f/<int:pk>/', include(book_router_forward.urls)),
    path('songs-api/',include(song_router.urls)),
    path('songs-api/<int:pk>/',include(song_router.urls)),
    path('singers-api/',include(singer_router.urls)),
    path('singers-api/<int:pk>/',include(singer_router.urls)),
]


