from django.contrib import admin

from app.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'public', 'repo_id', 'actor_id')
    list_filter = ('type', 'public')
    search_fields = ('type', 'repo_id', 'actor_id')
