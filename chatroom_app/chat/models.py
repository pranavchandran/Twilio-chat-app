from django.db import models

# Create your models here.

class Room(models.Model):
    # Chatrooms users can join

    name= models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        # Return human readable format
        return self.name

        