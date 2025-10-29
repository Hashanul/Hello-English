from django.db import models
from django.contrib.auth.models import User
from deep_translator import GoogleTranslator


class Banner(models.Model):
    # english inputs (what user will provide)
    title_english = models.CharField(max_length=255)
    subtitle_english = models.TextField(blank=True, null=True)
    button_english = models.CharField(max_length=100, blank=True, null=True)

    # bangla fields (auto-filled when blank)
    title_bangla = models.CharField(max_length=255, blank=True, null=True)
    subtitle_bangla = models.TextField(blank=True, null=True)
    button_bangla = models.CharField(max_length=100, blank=True, null=True)

    page = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='assets/uploads/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

    def save(self, *args, **kwargs):
        translator = GoogleTranslator(source='en', target='bn')

        if not self.title_bangla and self.title_english:
            self.title_bangla = translator.translate(self.title_english)

        if not self.subtitle_bangla and self.subtitle_english:
            self.subtitle_bangla = translator.translate(self.subtitle_english)

        if not self.button_bangla and self.button_english:
            self.button_bangla = translator.translate(self.button_english)


        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_english


    

class Instruction(models.Model):
    page = models.PositiveIntegerField(null=True, blank=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"Instruction Title: {self.title}"

class Content(models.Model):
    ins_title = models.ForeignKey(Instruction, related_name='contents', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Content: {self.content[:50]}"








# class Instruction(models.Model):
    # page = models.PositiveIntegerField(null=True, blank=True)
#     title = models.CharField(max_length=255)
#     content = models.TextField(help_text="List of instruction lines")
#     pdf = models.FileField(upload_to='instructions/pdfs/%Y/%m/%d/', blank=True, null=True )

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ['page']

#     def __str__(self):
#         return f"Page {self.page}: {self.title}"
    



