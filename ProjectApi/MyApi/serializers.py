from .models import City, Author, Book, Singer, Song
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
# ------------------------------- Reverse Serialization ------------------------------
# Order of serializer classes = reverse of order of their model classes


class BookSerializerReverse(ModelSerializer):

    class Meta:
        model = Book
        fields = ('id','book_name')


class AuthorSerializerReverse(ModelSerializer):

    class Meta:
        model = Author
        fields = ('id','author_name','author_age','books')
        # books is the related_name in Foreignkey field of Book model class.


class CitySerializerReverse(ModelSerializer):

    class Meta:
        model = City
        fields = ('id','city_name','country_name','authors')
        # authors is the related_name in Foreignkey field of Author model class.

# In the above examples no need to add any extra code to our serializers as we have related_field
# So, we can directly add to the fields tuple. By default, related_field in our models helps us to
# get primary keys of that model only. If we want other than pk we need to use serializers.<----> methods
# ------------------------ Forward Serialization --------------------------
# Order of serializer classes = order of their model classes


class CitySerializerForward(ModelSerializer):

    class Meta:
        model = City
        fields = ('id','city_name','country_name')


class AuthorSerializerForward(ModelSerializer):

    author_place = CitySerializerForward()
    class Meta:
        model = Author
        fields = ('id','author_name','author_age','author_place')


class BookSerializerForward(ModelSerializer):

    book_author = AuthorSerializerForward()
    class Meta:
        model = Book
        fields = ('id','book_name','book_author')

# ------------------------------------------------------------------------------------------------
# Until above 2 examples, we used pure serializer relationships ,Now let's see how to customize
# so that we can pass only required data to our api's in serializers.
# Here iam using the technique as,
# Order of serializer classes = reverse of order of their model classes


class SongSerializer(ModelSerializer):

    # singer_data1 = serializers.CharField(source='singer.singer_name')
    # singer_data2 = serializers.IntegerField(source='singer.id')
    # By default, 'singer' in fields list takes primary key of singer Model.
    # 'singer' is coming from ForeignKey field in Song model.
    # We can override as mentioned below,
    # singer = serializers.StringRelatedField(many=False, read_only=True)
    # singer = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    singer = serializers.SlugRelatedField(slug_field='singer_name',read_only='True',many=False)
    # Above 3 lines can be replaced by a grouping data as,
    # singer = SingerSerializer()
    # So, we can any of the above-mentioned methods.
    class Meta:
        model = Song
        fields = ('id','song_name','song_duration','singer')


class SingerSerializer(ModelSerializer):

    # songs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # songs = serializers.StringRelatedField(many=True,read_only=True) # uses __str__ method of Song Model
    # songs = serializers.SlugRelatedField(slug_field='song_duration',many=True, read_only='True')
    # NOTE : In slug_field we can use any of the fields which is in Song model class
    # We can use song_name / song_duration / id
    # Even we don't specify any of the above overriding things, drf considers PrimaryKeyRelatedField()
    # by default. So, Writing serializers.PrimaryKeyRelatedField() alone is of no use.
    # Else, I can use SongSerializer() as,
    songs = SongSerializer(many=True,read_only=True)
    class Meta:
        model = Singer
        fields = ('id','singer_name','songs')
    # If we use songs in fields alone, we will get all associated primary keys of Song Model as list()
    # songs is coming from related_name field from Foreignkey of song model.
    # If we override above the class Meta, we will get the type on which we serialized.











