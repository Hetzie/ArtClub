from django.db import models

# Create your models here.
class ArtStyle(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name