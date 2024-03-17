from rest_framework import serializers
from ailaysaapp.models import UserProfile,Category, Subcategory,PostModel, CommentModel

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'email', 'profile_picture']
        read_only_fields = ['id']
        
class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'subcategories']
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ['comment', 'publication_date']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    total_comments = serializers.SerializerMethodField()

    class Meta:
        model = PostModel
        fields = ['title', 'author', 'created_at', 'comments', 'total_comments']

    def get_total_comments(self, obj):
        return obj.comments.count()