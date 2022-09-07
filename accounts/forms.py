from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import ParagraphUser


class ParagraphUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = ParagraphUser
        fields = UserCreationForm.Meta.fields + ("name",)


class ParagraphUserChangeForm(UserChangeForm):
    class Meta:
        model = ParagraphUser
        fields = UserChangeForm.Meta.fields
