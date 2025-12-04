from django.db import models

class Visit(models.Model):
    count = models.IntegerField(default=0)  

    def __str__(self):
        return f"Licznik: {self.count}"