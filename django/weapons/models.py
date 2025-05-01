from django.db import models

class Weapon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    rarity = models.IntegerField(default=1)
    attack = models.JSONField(blank=True, null=True)      # Stores attack details like 'display'
    elements = models.JSONField(blank=True, null=True)    # List of elements with 'type' and 'damage'
    assets = models.JSONField(blank=True, null=True)      # Stores asset information like 'icon'
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name