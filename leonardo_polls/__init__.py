
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'leonardo_polls.Config'

class Default(object):

    optgroup = 'Polls'

    apps = [
        'leonardo_polls',
        'polls'
    ]

    widgets = [
        'leonardo_polls.widget.polls.models.PollsWidget'
    ]

    public = True

    @property
    def plugins(self):
        return [
            ('polls.urls', 'Polls'),
        ]


class Config(AppConfig):
    name = 'leonardo_polls'
    verbose_name = "leonardo-polls"

default = Default()