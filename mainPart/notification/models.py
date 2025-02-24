from django.db import models
class Notification(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Дата створення
    updated_at = models.DateTimeField(auto_now=True)  # Дата останнього оновлення
    is_read = models.BooleanField(default=False)  # Позначка про прочитання
    is_published = models.BooleanField(default=False)  # Позначка про публікації
