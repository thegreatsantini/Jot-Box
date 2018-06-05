from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class User(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField()

#     def __str__(self):
#         return "%s %s" % (self.first_name, self.last_name)


class Entry(models.Model):
    prompt = models.CharField(max_length=200)
    pub_date = models.DateField()
    notes = models.CharField(max_length=512)
    draft = models.CharField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.prompt

    class Meta:
        ordering = ('pub_date',)
