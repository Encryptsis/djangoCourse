from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)  # A string field for the project title with a max length
    description = models.TextField()  # A text field for a detailed project description
    image = models.ImageField()  # An image field to upload images to a specific folder
    created = models.DateTimeField(auto_now_add=True)  # A datetime field to automatically set the creation date
    updated = models.DateTimeField(auto_now=True)  # A datetime field to automatically update when the record is saved

    