from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=75, null=False, blank=False,
                            verbose_name='Задача')
    description = models.TextField(max_length=1000, null=True, blank=True,
                                   verbose_name='Описание')
    status = models.CharField(max_length=20, null=False, blank=False, default='new',
                              verbose_name='Готовность')

    def __str__(self):
        return "%s. %s (%s)"%(self.pk, self.name, self.status)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

