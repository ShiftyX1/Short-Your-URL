from django import forms
from django.forms import widgets

free_short_url_choices = (
    ('300', '5 минут'),
    ('1800', '30 минут'),
    ('3600', '60 минут'),
)

class FastShortUrl(forms.Form):
    input_url = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'Вставьте ссылку'}), label='')
    options_time = forms.ChoiceField(choices=free_short_url_choices, label='Время действия ссылки')


class FastGenerateQR(forms.Form):
    input_url_qr = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'Вставьте ссылку'}), label='')
    options_time_qr = forms.ChoiceField(choices=free_short_url_choices, label='Время действия QR-кода')

# widget=forms.widgets.ChoiceWidget(attrs={'class': 'form-select'}),