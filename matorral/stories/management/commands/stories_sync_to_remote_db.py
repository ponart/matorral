from django.core.management.base import BaseCommand

from matorral.sprints.models import Sprint
from matorral.users.models import User

from ...models import Epic, Story, StoryState


class Command(BaseCommand):
    help = "Sync local stories, states, epics & sprints to remote database"

    def handle(self, *args, **options):
        for user in User.objects.all():
            user.save(using='remote')

        for sprint in Sprint.objects.all():
            sprint.save(using='remote')

        for epic in Epic.objects.all():
            epic.save(using='remote')

        for state in StoryState.objects.all():
            state.save(using='remote')

        for story in Story.objects.all():
            story.save(using='remote')
