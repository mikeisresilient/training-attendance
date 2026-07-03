from django.contrib import admin

# Register your models here.
from .models import Participant


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "designation",
        "department",
        "phone_number",
        "email",
        "date_registered",
    )

    search_fields = (
        "full_name",
        "designation",
        "department",
        "email",
    )

    list_filter = (
        "department",
        "designation",
        "date_registered",
    )

    ordering = ("-date_registered",)