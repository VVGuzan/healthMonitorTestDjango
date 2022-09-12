from django.contrib import admin
from .models import TestInstance, UserSimple

# Register your models here.


@admin.register(TestInstance)
class TestInstanceAdmin(admin.ModelAdmin):
    list_display = ('display_test',)


@admin.register(UserSimple)
class UserSimpleAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'email')
