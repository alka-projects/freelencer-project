from django.contrib import admin
from apiapp.models import Categories, SubCategories, ImageTemplates, RenderImages

# Register your models here.
admin.site.register([Categories, SubCategories, ImageTemplates, RenderImages])
