from rest_framework import serializers

from blogit.apps.profiles.serializers import ProfileSerializer

from .models import Article,Comment,Tag
from .relations import TagRelatedField


class ArticleSerializer(serializers.ModelSerializer):

    author = ProfileSerializer(read_only=True)
    description = serializers.CharField(required=False)
    slug = serializers.SlugField(required=False)

    favourited=serializers.SerializerMethodField()
    favouritesCount=serializers.SerializerMethodField(method_name='get_favourites_count')

    tagList=TagRelatedField(many=True,required=False,source='tags')

    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Article
        fields = (
            'author',
            'body',
            'createdAt',
            'description',
            'favourited',
            'favouritesCount',
            'slug',
            'tagList',
            'title',
            'updatedAt',
        )

    def create(self, validated_data):
        author = self.context.get('author', None)
        tags=validated_data.pop('tags',[])
        article=Article.objects.create(author=author,**validated_data)

        for tag in tags:
            article.tags.add(tag)

        return article


    def get_created_at(self, instance):
        return instance.created_at.isoformat()

    def get_favourited(self,instance):
        request=self.context.get('request',None)

        if request is None:
            return False

        if not request.user.is_authenticated:
            return  False

        return request.user.profile.has_favourited(instance)

    def get_favourites_count(self,instance):
        return instance.favourited_by.count()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat()

class CommentSerializer(serializers.ModelSerializer):
    author=ProfileSerializer(required=False)
    createdAt=serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt=serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model=Comment
        fields=('id','author','body','createdAt','updatedAt')


    def create(self, validated_data):
        article=self.context['article']
        author=self.context['author']

        return Comment.objects.create(author=author,article=article,**validated_data)

    def get_created_at(self,instance):
        return instance.created_at.isoformat()

    def get_updated_at(self,instance):
        return instance.updated_at.isoformat()

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model=Tag
        fields=('tag',)

    def to_representation(self, obj):
        return obj.tag
