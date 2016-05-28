from django.contrib import admin

from .models import Player,News,Video,Live

class PlayerAdmin(admin.ModelAdmin):
	list_display = ('name','nick_name','home_display')

class NewsAdmin(admin.ModelAdmin):
	list_display = ('title','author','home_display')

class VideoAdmin(admin.ModelAdmin):
	list_display = ('video_name','home_display')

class LiveAdmin(admin.ModelAdmin):
	list_display = ('live_title','live_player','home_display')

admin.site.register(Player,PlayerAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(Video,VideoAdmin)
admin.site.register(Live,LiveAdmin)
