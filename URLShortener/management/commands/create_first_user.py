from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_model = get_user_model()

        if user_model.objects.all().count() == 0:
            print("Creating initial admin user...")
            user_model.objects.create_superuser(
                "admin", "", "admin"
            )
            print("Initial admin user created.")
        else:
            print("Users already exist. Skipping initial admin user creation.")
