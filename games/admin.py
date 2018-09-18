from django.contrib import admin

# Register your models here.

from .models import GameType, Player

class GameTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

#class PlayerAdmin(admin.ModelAdmin):
#    list_display = ('name', 'description')



admin.site.register(GameType, GameTypeAdmin)
admin.site.register(Player)



