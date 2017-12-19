from django.db import models
from django.utils.translation import ugettext as _


class Event(models.Model):
    title = models.CharField(
        name=_('title'),
        max_length=255,
    )
    description = models.TextField(
        name=_('full description'),
        default='',
    )
    creation_date = models.DateTimeField(
        verbose_name=_('creation date'),
        auto_now_add=True,
    )
    publish_date = models.DateTimeField(
        verbose_name=_('date of publication'),
        auto_now_add=True,
    )
    estimation_end_date = models.DateTimeField(
        verbose_name=_('time when event will be probably solved'),
        blank=False,
        null=True,
    )
    end_date = models.DateTimeField(
        verbose_name=_('real event end date'),
        blank=True,
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
        to='events.Event',
        related_name='bets',
        related_query_name='bet',
        on_delete=models.CASCADE
    )
    player = models.ForeignKey(
        to='accounts.Player',
        related_name='bets',
        related_query_name='bet',
        on_delete=models.CASCADE
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
