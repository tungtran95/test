from django.db import models

# Create your models here.
class Stackover(models.Model):
    question = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.question