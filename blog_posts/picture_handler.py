#blog_posts/picture_handler.py

import os
import uuid 
from PIL import Image 
from flask import url_for,current_app

def add_post_pic(pic_upload,username):

    filename = pic_upload.filename
    #mypicture . "jpeg"
    ext_type = filename.split('.')[-1]
    # "username.jpeg"

    unique_id = uuid.uuid4().hex
    storage_filename = f"{username}_{unique_id}.{ext_type}"
    print(storage_filename)

    filepath = os.path.join(current_app.root_path,'static', 'post_pics',storage_filename)

    output_size = (200,200)

    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename 