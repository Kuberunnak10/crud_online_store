from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Wear(models.Model):
    name = models.CharField(max_length=100)
    size = models.PositiveIntegerField()
    color = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


