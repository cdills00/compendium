from django.db import models

class Monster(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    species = models.CharField(max_length=50, blank=True)
    elements = models.JSONField(blank=True, null=True)      # List of strings
    weaknesses = models.JSONField(blank=True, null=True)    # List of dicts

    def __str__(self):
        return self.name