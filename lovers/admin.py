from django.contrib import admin

from lovers.models import Lover


@admin.register(Lover)
class LoverAdmin(admin.ModelAdmin):
    pass
