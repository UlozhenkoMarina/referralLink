from django.contrib import admin
from . import models

#registering of the botUser model
@admin.register(models.botUser)
class botUserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'referral_id', 'user_name']
    list_editable = ['referral_id', 'user_name']

#registering of the incorrectLink model
@admin.register(models.incorrectLink)
class incorrectLinkAdmin(admin.ModelAdmin):
    list_display = ['pk', 'referral_id', 'chat_id', 'frequency']
    list_editable = ['referral_id', 'chat_id', 'frequency']

