from django.core.management.base import BaseCommand
from pss.models import Registration

class Command(BaseCommand):
    help = 'List all registrations with detailed information'

    def add_arguments(self, parser):
        parser.add_argument('--membership-type', type=str, help='Filter by membership type')

    def handle(self, *args, **kwargs):
        membership_type = kwargs['membership_type']
        
        if membership_type:
            registrations = Registration.objects.filter(membership_type=membership_type)
        else:
            registrations = Registration.objects.all()

        for reg in registrations:
            self.stdout.write(
                f'Name: {reg.name}, Membership Type: {reg.membership_type}, Email: {reg.email}, '
                f'Phone: {reg.phone_number}, DOB: {reg.date_of_birth}, Address: {reg.address}, '
                f'Year at Panyango: {reg.year_at_panyango}, Occupation: {reg.occupation}, '
                f'Membership Fee: {reg.membership_fee}'
            )
