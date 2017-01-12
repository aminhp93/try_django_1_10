from django.core.management.base import BaseCommand, CommandError
# from polls.models import Question as Poll
from shortener.models import KirrURL

class Command(BaseCommand):
    help = 'Refresh all kirr url shortcode'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **options):
        print(options)
        # for poll_id in options['poll_id']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
        return KirrURL.objects.refresh_shortcodes(items = options['items'])
