
from django.db import models

# Model to store change log entries for database migrations and code clarity
class ChangeLog(models.Model):
    category = models.CharField(max_length=50)
    message = models.TextField()
    advice = models.TextField()

    def __str__(self):
        return f"{self.category}: {self.message[:30]}"
