from django.db import models
from django.utils.translation import gettext_lazy as _

class Subject(models.Model):
    class Meta:
        verbose_name = _("Расписание")
        verbose_name_plural = _("Расписания")
    name = models.CharField(max_length=50, verbose_name="Предмет")

    def __str__(self):
        return f"{self.name}"

class Schedule(models.Model):
    class Meta:
        verbose_name = _("Расписание")
        verbose_name_plural = _("Расписания")
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        verbose_name="Предмет"
    )
    start_time = models.TimeField(
        verbose_name="Время"
    )