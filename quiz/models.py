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
    page_en = models.PositiveIntegerField(null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)

    page_bn = models.CharField(max_length=50, null=True, blank=True)
    title_bn = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        translator = GoogleTranslator(source='en', target='bn')

        if not self.page_bn and self.page_en:
            self.page_bn = translator.translate(str(self.page_en))

        if not self.title_bn and self.title_en:
            self.title_bn = translator.translate(self.title_en)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Instruction Title: {self.title_en}"
        

class Content(models.Model):
    ins_title_en = models.ForeignKey(Instruction, related_name='contents', on_delete=models.CASCADE)
    content_en = models.TextField(null=True, blank=True)

    ins_title_bn = models.CharField(max_length=255, null=True, blank=True)
    content_bn = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        translator = GoogleTranslator(source='en', target='bn')

        if not self.ins_title_bn and self.ins_title_en and self.ins_title_en.title_en:
            self.ins_title_bn = translator.translate(self.ins_title_en.title_en)

        if not self.content_bn and self.content_en:
            self.content_bn = translator.translate(self.content_en)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Content: {self.content_en[:50]}"





    



