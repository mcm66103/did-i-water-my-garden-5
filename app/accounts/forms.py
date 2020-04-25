from django.forms import ModelForm
from accounts.models import Account

class NewAccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['email','password']

    def save(self):
        account = super().save(commit=False)
        account.set_password(self.cleaned_data["password"])
        account.save()
