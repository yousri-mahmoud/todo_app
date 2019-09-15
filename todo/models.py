from django.db import models

# Create your models here.


class Todo(models.Model):
    text = models.CharField(max_length=35)
    complet = models.BooleanField(default = False)


    def __str__(self):
        return self.text
    