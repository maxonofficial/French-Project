from django.db import models

from django.utils.translation import gettext_lazy as _

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Selection(TimeStamp):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

class department(Selection):
    def __str__(self):
        return self.name
    
class word(TimeStamp):
    english = models.TextField(_("English"))
    french = models.TextField(_("French"))
    department = models.ForeignKey(department, verbose_name=_("Department"), on_delete=models.CASCADE)

    def __str__(self):
        return self.english
