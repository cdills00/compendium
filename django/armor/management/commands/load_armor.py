import requests
from django.core.management.base import BaseCommand
from armor.models import Armor

class Command(BaseCommand):
    help = 'Load armor pieces from the Monster Hunter API into the database'

    def handle(self, *args, **kwargs):
        url = "https://mhw-db.com/armor"
        response = requests.get(url)
        if response.status_code != 200:
            self.stderr.write("Failed to fetch armor data")
            return

        for item in response.json():
            Armor.objects.update_or_create(
                name=item.get("name"),
                defaults={
                    "type": item.get("type", ""),
                    "rank": item.get("rank", ""),
                    "rarity": item.get("rarity", 1),
                    "defense": item.get("defense", {}),
                    "resistances": item.get("resistances", {}),
                    "slots": item.get("slots", []),
                    "skills": item.get("skills", []),
                    "armor_set": item.get("armorSet", {}),
                    "assets": item.get("assets", {}),
                    "crafting": item.get("crafting", {}),
                }
            )

        self.stdout.write(self.style.SUCCESS("Armor pieces loaded successfully."))