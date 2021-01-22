from django.db import models
from django.utils import timezone

class Service(models.Model):
    code = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    notes = models.TextField()
    address = models.TextField()
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.address
