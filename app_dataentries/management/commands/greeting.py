from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):
    help = "Greets the user"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("name", type=str, help="Specifies user name")

    def handle(self, *args, **kwargs):
        """Write the logic for hello world command"""
        name = kwargs.get("name", "Endang")

        self.stdout.write(self.style.SUCCESS("======================"))
        self.stdout.write(f"Hi {name}, Good Morning")
        self.stdout.write(self.style.SUCCESS("======================"))
