from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User as DjangoUser


class Lover(models.Model):
    user = models.OneToOneField(to=DjangoUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='lovers/', verbose_name=_("Lover image"), null=True, blank=True)
    profile_name = models.CharField(max_length=100, verbose_name=_("Profile name"), null=True, blank=True)

    def __str__(self):
        return f'{self.profile_name}'

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.image and hasattr(self.image, 'file'):
            self.image.name = f"LOVER_{self.user.username}"

        return super(Lover, self).save(force_insert, force_update, using, update_fields)
