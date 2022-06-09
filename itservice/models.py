from django.db import models

class Choose(models.Model):
    file = models.FileField(
        upload_to='images/%Y/%m/%d',
        blank=True,
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
    )
    description = models.TextField(
        blank=True,
    )
    def __str__(self):
        return self.title

class Service(models.Model):
    file = models.FileField(
        upload_to='images/%Y/%m/%d',
        blank=True,
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
    )
    description = models.TextField(
        blank=True,
    )
    def __str__(self):
        return self.title

class Product(models.Model):
    file = models.FileField(
        upload_to='images/%Y/%m/%d',
        blank=True,
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
    )
    mark = models.SmallIntegerField(
        default=0,
    )
    old_price = models.FloatField(
        blank=True,
    )
    new_price = models.FloatField(
        blank=True,
    )
    created = models.TimeField(
       auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )
    is_published = models.BooleanField(
        default=True,
    )
    def __str__(self):
        return self.title

class Feedback(models.Model):

    file = models.FileField(
        upload_to='images/%Y/%m/%d',
        blank=True,
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
    )
    number = models.IntegerField(
        blank=True,
    )
    def __str__(self):
        return self.title

class Testimonial(models.Model):
    file = models.FileField(
        upload_to='images/%Y/%m/%d',
        blank=True,
    )
    description = models.TextField(
        blank=True,
    )
    name = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
    )
    def __str__(self):
        return self.name

class Feedback(models.Model):
    website_url = models.URLField(
        max_length=200,
        blank=True,
    )
    your_name = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
    )
    email_address = models.EmailField(
        blank=True,
    )
    phone_number = models.CharField(
        max_length=18,
        blank=True,
    )
    message = models.TextField(
        blank=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )

