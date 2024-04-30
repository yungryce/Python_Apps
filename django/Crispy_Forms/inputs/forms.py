from django import forms
from .models import Candidate


class CandidateForm(forms.ModelForm):
    
    class Meta:
        model = Candidate
        fields = '__all__'
        # fields = ['first_name', 'last_name', 'email', 'message',]
        # exclude = ['email']