from django.contrib import admin

from .models import Participant


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('nim', 'name', 'department')
    search_fields = ('nim', 'name')
    list_filter = ('department',)
