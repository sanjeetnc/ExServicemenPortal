from django.db import models


class Circular(models.Model):

    title = models.CharField(
        max_length=250
    )

    pdf = models.FileField(
        upload_to='circulars/'
    )

    publish_date = models.DateField()

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title