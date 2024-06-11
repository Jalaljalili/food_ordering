from django import forms
from .models import Menu

class OrderForm(forms.Form):
    day_of_week = forms.ChoiceField(choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ])
    food_item = forms.ModelChoiceField(queryset=Menu.objects.none())

    def __init__(self, *args, **kwargs):
        day_of_week = kwargs.pop('day_of_week', None)
        super(OrderForm, self).__init__(*args, **kwargs)
        if day_of_week:
            self.fields['food_item'].queryset = Menu.objects.filter(day_of_week=day_of_week)
