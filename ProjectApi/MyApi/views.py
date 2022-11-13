from .models import City, Author, Book, Song, Singer
from rest_framework.viewsets import ModelViewSet
from .serializers import (CitySerializerReverse,
                          AuthorSerializerReverse,
                          BookSerializerReverse,
                          CitySerializerForward,
                          AuthorSerializerForward,
                          BookSerializerForward,
                          SongSerializer,
                          SingerSerializer,
                          )
from rest_framework.permissions import IsAuthenticated

class CityViewReverse(ModelViewSet):

    queryset = City.objects.all()
    serializer_class = CitySerializerReverse


class AuthorViewReverse(ModelViewSet):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializerReverse


class BookViewReverse(ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializerReverse


class CityViewForward(ModelViewSet):

    queryset = City.objects.all()
    serializer_class = CitySerializerForward


class AuthorViewForward(ModelViewSet):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializerForward


class BookViewForward(ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializerForward


class SongView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SingerView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

