from django.db import models
from django.db.models import query
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from apiapp.serializers import CategoriesSerializer, SubCategoriesSerializer, ImageTemplatesSerializer, RenderImagesSerializer
from apiapp.models import Categories, SubCategories, ImageTemplates, RenderImages

# Create your views here.
class CategoriesApiViews(ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()
    

class SubCategoriesApiViews(ModelViewSet):
    serializer_class = SubCategoriesSerializer
    queryset = SubCategories.objects.all()
    

class ImageTemplatesApiViews(ModelViewSet): 
    serializer_class = ImageTemplatesSerializer
    queryset = ImageTemplates.objects.all()
 

class RenderImagesApiViews(ModelViewSet): 
    serializer_class = RenderImagesSerializer
    queryset = RenderImages.objects.all() 


