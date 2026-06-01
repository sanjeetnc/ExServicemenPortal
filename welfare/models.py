from django.db import models
from django.utils.text import slugify


class WelfareScheme(models.Model):

    title = models.CharField(max_length=200)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    short_description = models.TextField()

    description = models.TextField()

    eligibility = models.TextField()

    benefits = models.TextField()

    image = models.ImageField(
        upload_to='welfare/'
    )

    is_featured = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title