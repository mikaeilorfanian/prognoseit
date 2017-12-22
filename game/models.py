from django.db import models
from django.utils.translation import ugettext as _
from account.models import Player


class Event(models.Model):
    title = models.CharField(
        max_length=255,
        name=_('title'),
    )
    description = models.TextField(
        default='',
        name=_('full description'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('creation date'),
    )
    published_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('date of publication'),
    )
    estimated_end_date = models.DateTimeField(
        blank=False,
        verbose_name=_('time when event will be probably solved'),
        null=True,
    )
    ended_at = models.DateTimeField(
        blank=True,
        verbose_name=_('real event end date'),
        null=True,
    )
    price = models.IntegerField(
        default=50,
        name=_('bet price'),
    )


class Bet(models.Model):
    YES = True
    NO = False
    BET_OUTCOME_CHOICES = (
        (YES, _('YES prediction')),
        (NO, _('NO prediction')),
    )

    event = models.ForeignKey(
        to=Event,
        related_name='bets',
        related_query_name='bet',
    )
    player = models.ForeignKey(
        to=Player,
        related_name='bets',
        related_query_name='bet',
    )
    outcome = models.BooleanField(
        choices=BET_OUTCOME_CHOICES,
        help_text=_('Check if YES prediction else prediction is NO'),
        verbose_name=_('YES prediction'),
    )
    quantity = models.PositiveIntegerField(
        default=0,
        null=False,
        verbose_name=_('number of bets'),
    )
