import requests
from django.core.management.base import BaseCommand
from weapons.models import Weapon

class Command(BaseCommand):
    help = 'Load weapons from the Monster Hunter API into the database'

    def handle(self, *args, **kwargs):
        url = "https://mhw-db.com/weapons"
        response = requests.get(url)
        if response.status_code != 200:
            self.stderr.write("Failed to fetch weapons")
            return

        for item in response.json():
            Weapon.objects.update_or_create(
                name=item.get("name"),
                defaults={
                    "type": item.get("type", ""),
                    "rarity": item.get("rarity", 1),
                    "attack": item.get("attack", {}),
                    "elements": item.get("elements", []),
                    "assets": item.get("assets", {}),
                }
            )

        self.stdout.write(self.style.SUCCESS("Weapons loaded successfully."))