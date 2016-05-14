# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from leonardo.module.web.models import Page, Widget
from polls.models import Poll

class PollsWidget(Widget):

    poll = models.ForeignKey('polls.Poll', verbose_name='Poll')

    class Meta:
        abstract = True
        verbose_name = _('Poll')
        verbose_name_plural = _('Polls')