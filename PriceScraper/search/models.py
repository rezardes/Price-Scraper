from django.db import models

class Produk(models.Model):
	name = models.CharField(max_length=128)
	price = models.IntegerField(default=0)
	imageURL = models.URLField()

	def __str__(self):
		return self.name