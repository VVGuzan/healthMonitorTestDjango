from calendar import c
from django.contrib import admin
from .models import TestInstance, UserSimple

# Register your models here.


@admin.register(TestInstance)
class TestInstanceAdmin(admin.ModelAdmin):
    list_display = ("display_test",)
    # readonly_fields = ["formatted_test_date", "id"]
    fieldsets = (
        (None, {"fields": ("user",)}),
        (
            "Test information",
            {
                "classes": ["collapse"],
                "fields": [
                    (
                        "formatted_test_date",
                        "id",
                    )
                ],
            },
        ),
        ("Test results", {"fields": [("acet", "keto", "par", "rpm")]}),
        (
            "Additional information",
            {"classes": ["collapse"], "fields": ["type", "comment"]},
        ),
    )


class TestInstanceInline(admin.TabularInline):
    model = TestInstance
    extra: int = 0
    # readonly_fields = ["formatted_test_date", "id"]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "formatted_test_date",
                    ("acet", "keto", "par", "rpm"),
                    ("type",),
                    "id",
                ]
            },
        ),
    ]


@admin.register(UserSimple)
class UserSimpleAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "email")
    fields = [("last_name", "first_name"), "date_of_birth", "email"]
    inlines = [
        TestInstanceInline,
    ]
