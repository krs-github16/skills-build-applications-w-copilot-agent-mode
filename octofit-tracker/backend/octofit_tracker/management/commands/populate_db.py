from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        User.objects.create(email='john.doe@example.com', name='John Doe', age=16)
        User.objects.create(email='jane.smith@example.com', name='Jane Smith', age=17)

        # Create test teams
        team1 = Team.objects.create(name='Team Alpha')
        team2 = Team.objects.create(name='Team Beta')

        team1.members.add(User.objects.get(email='john.doe@example.com'))
        team2.members.add(User.objects.get(email='jane.smith@example.com'))

        # Create test activities
        Activity.objects.create(user=User.objects.get(email='john.doe@example.com'), type='Running', duration=30, date='2025-05-30')
        Activity.objects.create(user=User.objects.get(email='jane.smith@example.com'), type='Walking', duration=45, date='2025-05-30')

        # Create test leaderboard entries
        Leaderboard.objects.create(user=User.objects.get(email='john.doe@example.com'), points=100)
        Leaderboard.objects.create(user=User.objects.get(email='jane.smith@example.com'), points=150)

        # Create test workouts
        Workout.objects.create(name='Morning Run', description='A quick morning run to start the day.', duration=30)
        Workout.objects.create(name='Evening Walk', description='A relaxing walk in the evening.', duration=45)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
