from django.db import models


class Tag(models.Model):

    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag


class Task(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    deadline = models.DateTimeField(null=True, blank=True)
    do_status = models.BooleanField(default=False)
