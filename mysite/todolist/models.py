from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    title = models.CharField(verbose_name="Pavadinimas", max_length=100, default="")
    task_text = models.TextField(verbose_name="Aprašymas", max_length=100, blank=True)
    is_done = models.BooleanField(verbose_name="Ar atlikta", default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date"]

