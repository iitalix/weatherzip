# Custom runserver command to simplify starting Redis + Django server
import subprocess

from django.core.management.commands.runserver import Command as RunserverCommand


class Command(RunserverCommand):
    def handle(self, *args, **options):
        try:
            print("Starting Redis server...")
            subprocess.run(["brew", "services", "start", "redis"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to start Redis: {e}")

        # Call the original runserver command
        super().handle(*args, **options)
