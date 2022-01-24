from django.contrib import admin

from sponsorship.models import Association, Goddaughter, Godfather, Preferences

# Register your models here.
admin.site.register(Preferences)
admin.site.register(Godfather)
admin.site.register(Goddaughter)
admin.site.register(Association)
