from django.db import models
import os

def image_upload_path(instance, filename):
    # Construct the file path based on the username and original filename
    username = instance.username
    image_name, image_ext = os.path.splitext(filename)
    new_filename = f"{username}{image_ext}"
    return os.path.join("img", username, new_filename)

class Image(models.Model):
    username = models.CharField(max_length=100)
    image = models.ImageField(upload_to=image_upload_path)

    def __str__(self):
        return self.username
