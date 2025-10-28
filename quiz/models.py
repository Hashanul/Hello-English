from django.db import models
from django.contrib.auth.models import User


class Banner(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='banner/%Y/%m/%d/', blank=True, null=True)
    button = models.CharField(max_length=100, blank=True, null=True)
    page = models.CharField(max_length=100, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']


class Instruction(models.Model):
    page = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField(help_text="List of instruction lines")
    pdf = models.FileField(upload_to='instructions/pdfs/%Y/%m/%d/', blank=True, null=True )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['page']

    def __str__(self):
        return f"Page {self.page}: {self.title}"
    
    

    def __str__(self):
        return f"Banner : {self.title}"




