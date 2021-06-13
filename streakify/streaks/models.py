from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from datetime import date

class Streak(TimeStampedModel):
    STREAK_TYPES = (
        ("Definite", "Definite"),
        ("Indefinite", "Indefinite"),
    )
    streak_type = models.CharField(
        _("Type of Streak"), choices=STREAK_TYPES, max_length=50)
    name = models.CharField(_("Streak Name"), max_length=100)
    max_duration = models.PositiveIntegerField(_("Maximum Duration in days"), default=1)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=False, null=False,
                              related_name="streak_user")

    def __str__(self):
        return self.name


class StreakRecord(TimeStampedModel):
    participant = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=False, null=False,
                              related_name="streak_participant")
    streak =  models.ForeignKey('streaks.Streak', on_delete=models.CASCADE, blank=False, null=False,
                              related_name="streak")
    start_date = models.DateField(_("User started from"), default=date.today)
    punch_in = models.BooleanField(default=False)

    def __str__(self):
        return "{}:{}".format(self.streak, self.participant)