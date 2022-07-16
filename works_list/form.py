from django import forms
from django.core.exceptions import ValidationError

from works_list.models import ZeroLevel


class AddWorkForm(forms.ModelForm):
    # form for adding new work/task
    class Meta:
        model = ZeroLevel
        fields = ['name',
                  ]
