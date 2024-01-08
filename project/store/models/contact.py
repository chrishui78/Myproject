from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(default='', blank=True, null= True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

