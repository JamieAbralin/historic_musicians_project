# musicians/models.py
from django.db import models

class Musician(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Musicians"

class MusicianPortrait(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='musician_portraits/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Portrait of {self.musician.name}"
