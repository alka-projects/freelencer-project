from rest_framework import serializers
from apiapp.models import Categories, SubCategories, ImageTemplates, RenderImages


class CategoriesSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Categories
        fields = '__all__'


class SubCategoriesSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = SubCategories
        fields = '__all__'
    
class ImageTemplatesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ImageTemplates
        fields = '__all__'

class RenderImagesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = RenderImages
        fields = '__all__'