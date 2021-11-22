from django.db import models
from uuid import uuid4


class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    used_book = models.BooleanField()
    pages_count = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.author} - {self.release_year}'

