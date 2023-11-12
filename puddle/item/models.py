from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

        
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(blank= True, null=True)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name="item", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)