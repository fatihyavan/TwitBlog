from django.db import models

class Tweets(models.Model):
    title=models.CharField(max_length=50,verbose_name="isim")
    text=models.TextField(max_length=144,verbose_name="Mesaj")
    completed=models.BooleanField(verbose_name="durum")

    def __str__(self):
       return self.title



