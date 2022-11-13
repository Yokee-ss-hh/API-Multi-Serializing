from django.db import models


class City(models.Model):

    city_name = models.CharField(max_length=200, verbose_name='city name')
    country_name = models.CharField(max_length=200, verbose_name='country name')

    def __str__(self):
        return f'{self.city_name} : {self.country_name}'

    class Meta:
        db_table = 'citytable'
        verbose_name = 'city'


class Author(models.Model):

    author_name = models.CharField(max_length=200, verbose_name='author name')
    author_age = models.IntegerField(verbose_name='author age')
    author_place = models.ForeignKey(to=City, related_name='authors',on_delete=models.CASCADE)

    def __str__(self):
        return self.author_name

    class Meta:
        db_table = 'authortable'
        verbose_name = 'author'


class Book(models.Model):

    book_name = models.CharField(max_length=200, verbose_name='book name')
    book_author = models.ForeignKey(to=Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.book_name} by {self.book_author}'

    class Meta:
        db_table = 'booktable'
        verbose_name = 'book'


class Singer(models.Model):

    singer_name = models.CharField(max_length=200, verbose_name='singer name')

    def __str__(self):
        return self.singer_name

    class Meta:
        db_table = 'singertable'
        verbose_name = 'singer'


class Song(models.Model):

    song_name = models.CharField(max_length=200, verbose_name='song name')
    singer = models.ForeignKey(to=Singer, on_delete=models.CASCADE, related_name='songs')
    song_duration = models.IntegerField()

    def __str__(self):
        return self.song_name

    class Meta:
        db_table = 'songtable'
        verbose_name = 'song'







