from django.db import models

class Feedback(models.Model):
        id = models.AutoField(primary_key=True)
        email = models.EmailField(null=False, blank=False)
        message  = models.TextField(null=False, blank=False)
        createdAt = models.DateTimeField(auto_now_add=True)