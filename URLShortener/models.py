from django.contrib.auth.models import User
from django.db import models
from django.utils.crypto import get_random_string

class URLRedirect(models.Model):
    original_URL = models.URLField()
    short_URL_suffix = models.CharField(max_length=6, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    access_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs) -> None:
        if not self.short_URL_suffix:
            new_suffix = get_random_string(length=6)

            while URLRedirect.objects.filter(short_URL_suffix = new_suffix).exists():
                new_suffix = get_random_string(length=6)
            
            self.short_URL_suffix = new_suffix

        super().save(*args, **kwargs)
