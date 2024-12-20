from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False)

    title = models.CharField(max_length=200,
                             blank=False)

    description = models.TextField(null=True,
                                   blank=True)

    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed']
