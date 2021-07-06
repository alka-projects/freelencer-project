# API PROJECT

## Description

- This Project Takes Data from API and performs all  CRUD Operations related to specific table. 
- You have to install all requirements from requirements.txt 
- You have to make migrations by using `python manage.py makemigrations` command from terminal 
- Then you have to make migrage by using `python manage.py migrate` command from terminal 
- Then to start server type `python manage.py runserver` in the terminal.

- Go to browser hit the url `http://127.0.0.1:8000`


## Models 


- `Categories` table take all fields related to Categories. 

    | Field | type |
    |-------|---------|
    |`title`|  CharField|
    |`category_name` |  CharField|
    |`icon`|  ImageField|
    |`status`|  BooleanField|


- `SubCategories` table take all fields related to SubCategories such as. 
    | Field | type |
    |-------|---------|
    | `cat_id` | `ForeignKey` from Categories table |
    |`title`|  CharField|
    |`category_name` |  CharField|
    |`icon`|  ImageField|
    |`status`|  BooleanField|

- `ImageTemplates` table takes field such as 

    | Field | type |
    |-------|---------|
    |`cat_id`| ForeignKey from Categories|
    | `sub_cat_id`| ForeignKey from SubCategories| table
    | `img_title`|  text field| 
    | `img_icon`|  ImageField|
    | `img_suprise_text_1`|   TextField|
    | `img_suprise_text_3`|   TextField|
    | `img_suprise_text_2`|   TextField|
    | `img_suprise_text_3`|   TextField|
    | `img_suprise_text_4`|   TextField|
    | `img_suprise_text_5`|   TextField|
    | `img_suprise_text_6`|   TextField|
    | `img_suprise_text_7`|   TextField|
    | `img_suprise_text_8`|   TextField|
    | `img_suprise_text_9`|   TextField|
    | `img_suprise_text_10`|  TextField|
    | `img_text_place_position`|  CharField|
    | `img_text_font_size`|  CharField|
    | `img_text_font` |   CharField|
    | `img_overlay_dim`|  CharField|
    | `img_overlay_position` |  CharField|
    | `img_stamp_1` |     ImageField|
    | `img_stamp_1_position`|  CharField|
    | `img_stamp_2`  |    ImageFields|
    | `img_stamp_2_position` | CharField|
    | `img_background_low` |  ImageField|
    | `img_background_hd` |  ImageField|
    | `status`  |   BooleanField|

- `RenderImages` table take all fields related to SubCategories such as.
    | Field | Type | 
    |-------|------|
    | `img_template_id` | ForeignKey from mageTemplates | 
    | `img_overlay` | `URLField` (image URL from s3 - mobile app will save to this, open CV will get image from here) | 
    | `generated_img_low`| `URLField` (image URL from s3, open CV script will post here)
    | `generated_img_hd` |   `URLField` (image URL from s3, open CV script will post here)
    | `share_on_twitter_text` | TextField | 
    | `share_on_facebook_text` | TextField | 
    | `share_on_insta_text` | TextField | 

### Note: 

- `CharField` take max 250 characters.


##  API Routes

##### All the routes are capable for CRUD operation.

- `http://localhost:8000/Categories`
- `http://localhost:8000/SubCategories`
- `http://localhost:8000/ImageTemplates`
- `http://localhost:8000/RenderImages`



