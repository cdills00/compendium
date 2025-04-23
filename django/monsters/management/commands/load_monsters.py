import requests
from django.core.management.base import BaseCommand
from monsters.models import Monster

class Command(BaseCommand):
    help = 'Fetch and store monsters from the MHW API'

    def handle(self, *args, **kwargs):
        url = "https://mhw-db.com/monsters"
        response = requests.get(url)

        if response.status_code != 200:
            self.stderr.write("Failed to fetch data.")
            return

        data = response.json()

        for item in data:
            Monster.objects.update_or_create(
                name=item.get("name"),
                defaults={
                    "type": item.get("type", ""),
                    "species": item.get("species", ""),
                    "elements": item.get("elements", []),
                    "weaknesses": item.get("weaknesses", []),
                }
            )
        self.stdout.write(self.style.SUCCESS("Monsters loaded into database."))