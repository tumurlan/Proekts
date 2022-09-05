from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name

