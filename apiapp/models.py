from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.

class Categories(models.Model):
    title = models.CharField(max_length=250)
    category_name = models.CharField(max_length=250)
    icon = models.ImageField()
    status = models.BooleanField()
    
    
class SubCategories(models.Model):
    cat_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    subcategory_name = models.CharField(max_length=250)
    icon = ImageField()
    status = models.BooleanField()
    
    
class ImageTemplates(models.Model):
    cat_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    sub_cat_id = models.ForeignKey(SubCategories, on_delete=models.CASCADE)
    img_title = models.CharField(max_length=250)
    img_icon = models.ImageField()
    img_surprise_text_1 = models.TextField()
    img_surprise_text_2 = models.TextField()
    img_surprise_text_3 = models.TextField()
    img_surprise_text_4 = models.TextField()
    img_surprise_text_5 = models.TextField()
    img_surprise_text_6 = models.TextField()
    img_surprise_text_7 = models.TextField()
    img_surprise_text_8 = models.TextField()
    img_surprise_text_9 = models.TextField()
    img_surprise_text_10 = models.TextField()
    img_text_place_position = models.CharField(max_length=250)
    img_text_font_size = models.CharField(max_length=250)
    img_text_font = models.CharField(max_length=250)
    img_overlay_dim = models.CharField(max_length=250)
    img_overlay_position = models.CharField(max_length=250)
    img_stamp_1 = models.ImageField()
    img_stamp_1_position = models.CharField(max_length=250)
    img_stamp_2 = models.ImageField()
    img_stamp_2_position = models.CharField(max_length=250)
    img_background_low = models.ImageField()
    img_background_hd = models.ImageField()
    status = models.BooleanField()
    
    
class RenderImages(models.Model): 
    img_template_id = models.ForeignKey(ImageTemplates, on_delete=models.CASCADE)   
    img_overlay = models.URLField()
    generated_img_low = models.URLField()
    generate_img_hd = models.URLField()
    share_on_twitter_text = models.TextField()
    share_on_facebook_text = models.TextField()
    share_on_insta_text = models.TextField()
    