from django import forms
from .models import Reg, Category

#added new model
choices = Category.objects.all().values_list('name', 'name')
# choice_list = []
# for items in choices:
#     choice_list.append(items)

class Postform(forms.ModelForm):
    class Meta:
        model = Reg
        fields = ('title', 'title_tag', 'author', 'category', 'body')
        # to replace fields on template
        labels = {
        'title': 'Title',
        'title_tag': 'Tag',
        'author': 'Writer',
        'category': 'Branch',
        'body': 'Text',
        'pub_date': '',
        }


        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Post Title'}),
            'author': forms.Select(attrs={'class' : 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class' : 'form-control'}),
            'body': forms.Textarea(attrs={'class' : 'form-control'}),
            'pub_date': forms.DateTimeField
        }


class Editform(forms.ModelForm):
    class Meta:
        model = Reg
        fields = ('title', 'title_tag', 'category', 'body')
    
        labels = {
        'title': 'Title', 
        'title_tag': 'Tag',
        # 'author': 'Writer',
        'category': 'Branch',
        'body': 'Text',
        }


        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Post Title'}),
            'category': forms.Select(choices=choices, attrs={'class' : 'form-control'}),
            'body': forms.Textarea(attrs={'class' : 'form-control'}),
        }