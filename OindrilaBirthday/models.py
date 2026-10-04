from django.db import models

class BirthdayWish(models.Model):
    guest_name = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f"{self.guest_name}: {self.text}"