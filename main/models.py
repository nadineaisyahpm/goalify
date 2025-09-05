from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, default="Unnamed Product")
    price = models.IntegerField(default=0)
    description = models.TextField(default="", blank=True)
    thumbnail = models.URLField(default="https://via.placeholder.com/300")  # untuk link gambar
    category = models.CharField(max_length=100, default="General")
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name