# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from leonardo.module.web.models import Page, Widget

class PollsWidget(Widget):

    title = models.CharField(max_length=255, default="What's up?")

    class Meta:
        abstract = True
        verbose_name = _('Poll')
        verbose_name_plural = _('Polls')