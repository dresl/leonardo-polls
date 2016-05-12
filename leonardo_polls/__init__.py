
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'leonardo_polls.Config'

LEONARDO_APPS = [
    'polls',
]

LEONARDO_PUBLIC = True

class Default(object):

    optgroup = 'Polls'

    apps = [
        'leonardo_polls'
    ]

    widgets = [
        'leonardo_polls.widget.polls.models.PollsWidget'
    ]


class Config(AppConfig):
    name = 'leonardo_polls'
    verbose_name = "leonardo-polls"

default = Default()