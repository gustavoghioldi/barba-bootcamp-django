from django.forms import ModelForm
from polls.models import Choice

class VoteForm(ModelForm):
    class Meta:
        model = Choice
        fields = "__all__"
