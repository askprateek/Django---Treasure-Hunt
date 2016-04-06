from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Player, Question

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class PlayerInline(admin.StackedInline):
    model = Player
    can_delete = False
    verbose_name_plural = 'Player'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (PlayerInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Question)
