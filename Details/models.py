from django.db import models

# Create your models here.
class ArtStyle(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Mentor(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    art_style = models.ForeignKey(ArtStyle, on_delete=models.CASCADE, related_name='art_style')
    contact_number = models.BigIntegerField(unique=True)
    email = models.EmailField(unique=True)
    salary = models.BigIntegerField()

    def __str__(self):
        split_email = self.email.split('@')
        return split_email[0]