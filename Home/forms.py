from django.forms import ModelForm
from .models import Transaction,Advert


class Transaction_form(ModelForm):
    class Meta:
        model = Transaction
        fields = ("amount","email")

class Advert_form(ModelForm):
    class Meta:
        model = Advert
        fields= ("task","slide")

