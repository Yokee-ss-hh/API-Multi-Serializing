from django.contrib import admin
from .models import Book, Author, City, Singer, Song

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(City)
admin.site.register(Singer)
admin.site.register(Song)


