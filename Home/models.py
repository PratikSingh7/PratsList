from django.db import models


class Search(models.Model):
    search = models.TextField(max_length=500)

    def __str__(self):
        return '{}'.format(self.search)

    class Meta:
        verbose_name_plural = 'Searches'
