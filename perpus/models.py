from django.db import models


class Buku(models.Model):
  judul = models.CharField(max_length=200)
  publish = models.DateTimeField("tanggal Publikasi")


  def __str__(self):
      return self.judul


# Create your models here.
