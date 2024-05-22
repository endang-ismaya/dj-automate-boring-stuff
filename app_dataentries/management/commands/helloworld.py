from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Prints Hello World"

    def handle(self, *args, **kwargs):
        """Write the login for hello world command"""
        self.stdout.write("Hello World")
