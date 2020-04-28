from django.db import models

# Create your models here.


class Test(models.Model):
    title = models.CharField(max_length=100)
    phone = models.IntegerField()
    image = models.ImageField(default='default.jpg', blank=True, null=True)

    def __str__(self):
        return self.title