from django.db import models

class Armor(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20)  # e.g., head, chest, arms, waist, legs
    rank = models.CharField(max_length=20)  # e.g., low, high, master
    rarity = models.IntegerField()
    defense = models.JSONField(blank=True, null=True)       # base, max, augmented
    resistances = models.JSONField(blank=True, null=True)   # fire, water, ice, thunder, dragon
    slots = models.JSONField(blank=True, null=True)         # list of slot dicts
    skills = models.JSONField(blank=True, null=True)        # list of skill dicts
    armor_set = models.JSONField(blank=True, null=True)     # id, name, rank, pieces
    assets = models.JSONField(blank=True, null=True)        # icon, imageMale, imageFemale
    crafting = models.JSONField(blank=True, null=True)      # materials list
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name