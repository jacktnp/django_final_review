from django.db import models

class Catalog(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Shop(models.Model):
    title = models.CharField(max_length=100)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
