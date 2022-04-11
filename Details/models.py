from django.db import models

# Create your models here.
class ArtStyle(models.Model):
    id = models.IntegerField(primary_key=True)
    # name = models.CharField(max_length=50)
    class Style(models.TextChoices):
        PAINTING = 'PNT','Painting'
        SCULPTURE = 'SCP','Sculpture'
        POP_ART = 'PA','Pop_art'
        SKETCHING = 'SKH','Sketching'
        CRAFT = 'CFT','Craft'
    style = models.CharField(max_length=30, choices=Style.choices)

    def __str__(self):
        return self.style

class Mentor(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    art_style = models.ForeignKey(ArtStyle, on_delete=models.CASCADE, related_name='art_style')
    contact_number = models.BigIntegerField(unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        split_email = self.email.split('@')
        return split_email[0]

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    art_style = models.ForeignKey(ArtStyle, on_delete=models.CASCADE, related_name='artstyle')
    contact_number = models.BigIntegerField(unique=True)
    email = models.EmailField(unique=True)
    rank = models.IntegerField()

    def __str__(self):
        split_email = self.email.split('@')
        return split_email[0]
