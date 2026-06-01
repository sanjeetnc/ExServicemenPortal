from django.db import models


class TrustActivity(models.Model):

    title = models.CharField(
        max_length=250
    )

    image = models.ImageField(
        upload_to='trust/'
    )

    description = models.TextField()

    event_date = models.DateField()

    location = models.CharField(
        max_length=200,
        blank=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title