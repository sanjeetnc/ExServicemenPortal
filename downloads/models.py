from django.db import models


class Download(models.Model):

    CATEGORY_CHOICES = [
        ('forms', 'Forms'),
        ('pension', 'Pension'),
        ('welfare', 'Welfare'),
        ('education', 'Education'),
        ('trust', 'Trust'),
        ('other', 'Other'),
    ]

    title = models.CharField(
        max_length=200
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    file = models.FileField(
        upload_to='downloads/'
    )

    description = models.TextField(
        blank=True
    )

    download_count = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title