from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User


class Player(User):
    is_vip = models.BooleanField(
        default=False,
        name='VIP',
        verbose_name=_('Very Important Person'),
        help_text=_('Check if player is Very Important Person'),
    )

    class Meta:
        verbose_name = _('player')
        verbose_name_plural = _('players')
