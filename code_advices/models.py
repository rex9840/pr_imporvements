from django.db import models
from django.conf import settings

# Model to store change log entries for database migrations and code clarity
class CodeAdvice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='code_advices')
    category = models.CharField(max_length=50)
    message = models.TextField()
    advice = models.TextField()

    def __str__(self):
        return f"{self.category}: {self.message[:30]}"
