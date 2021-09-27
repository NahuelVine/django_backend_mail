from django.db import models

# Create your models here.
class Registrado(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    timeStamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.email