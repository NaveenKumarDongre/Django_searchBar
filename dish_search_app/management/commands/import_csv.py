import csv
from django.core.management.base import BaseCommand
from dish_search_app.models import Dish_data  


class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to CSV file')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']
        with open(csv_file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Dish_data.objects.create(
                id=row['id'],
                name=row['name'],
                location=row['location'],
                items=row['items'],
                lat_long=row['lat_long'],
                full_details=row['full_details']
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))
