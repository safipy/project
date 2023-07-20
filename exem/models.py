from django.db import models


class Exem(models.Model):
    id_exem = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
