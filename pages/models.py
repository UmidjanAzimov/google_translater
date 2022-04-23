from django.db import models

# Create your models here.
class Translater(models.Model):
    english = models.TextField()
    uzbek = models.TextField()

    def __str__(self):
        return self.english + ' to  ' + self.uzbek