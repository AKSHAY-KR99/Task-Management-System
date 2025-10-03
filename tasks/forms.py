from django import forms

from .models import CustomUser, Task


class SimpleUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "role")

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match!")

        return cleaned_data


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "assigned_to", "due_date"]
        widgets = {
            "due_date": forms.DateInput(
                attrs={"type": "date"}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["assigned_to"].queryset = CustomUser.objects.exclude(role="super_admin")



from django import forms
from .models import Task, CustomUser

class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "assigned_to", "assigned_by", "due_date", "status", "completion_report", "worked_hours"]
        widgets = {
            "due_date": forms.DateInput(attrs={"type": "date"})
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

        if user.role == "super_admin":
            return

        elif user.role == "admin":
            for field in self.fields:
                if field != "assigned_to":
                    self.fields[field].disabled = True
            self.fields["assigned_to"].queryset = CustomUser.objects.exclude(role="super_admin")

        elif user.role == "user":
            for field in self.fields:
                if field not in ["status", "completion_report", "worked_hours"]:
                    self.fields[field].disabled = True



class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "role"]