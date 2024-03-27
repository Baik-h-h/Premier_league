import csv
from django.core.management.base import BaseCommand
from premier_league.models import Player

class Command(BaseCommand):
    help = 'Imports players data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        
        # Open the CSV file and iterate over its rows
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                point, goals = eval(row['p/g_goal'])  # Evaluating the string representation of the list to get the actual list

                # Create or update the Player object
                player, created = Player.objects.get_or_create(
                    name=name,
                    defaults={'point': point, 'goals': goals}
                )

                if not created:
                    player.point = point
                    player.goals = goals
                    player.save()

        self.stdout.write(self.style.SUCCESS('Players data imported successfully'))
