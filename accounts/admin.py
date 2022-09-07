from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ParagraphUserCreationForm, ParagraphUserChangeForm
from .models import ParagraphUser


class ParagraphUserAdmin(UserAdmin):
    add_form = ParagraphUserCreationForm
    form = ParagraphUserChangeForm
    model = ParagraphUser
    list_display = [
        "name",
        "username",
        "email",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)


admin.site.register(ParagraphUser, ParagraphUserAdmin)
