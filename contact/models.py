from django.db import models

class Enquiry(models.Model):

    CATEGORY_CHOICES = (
        ('Ex-Serviceman', 'Ex-Serviceman'),
        ('Widow', 'Widow'),
        ('Dependent', 'Dependent'),
        ('Serving Personnel', 'Serving Personnel'),
    )

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    )

    full_name = models.CharField(max_length=200)

    mobile = models.CharField(max_length=20)

    email = models.EmailField()

    service_number = models.CharField(
        max_length=100,
        blank=True
    )

    rank = models.CharField(
        max_length=100,
        blank=True
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    subject = models.CharField(max_length=250)

    message = models.TextField()

    document = models.FileField(
        upload_to='enquiries/',
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.full_name