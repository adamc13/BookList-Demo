from django.db import models

# Create your models here.


class Books (models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.title
