from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

