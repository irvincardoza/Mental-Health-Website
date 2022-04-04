from django import forms
from inno_app.models import Upload

class UploadForm(forms.ModelForm):
    first_name= forms.CharField(label='',required=False,widget=forms.TextInput(attrs={'placeholder':'Enter your name or leave blank(anonymous)','style':'width:400px;','class':'form-control'}))
    story_text = forms.CharField(label='',required=False, widget=forms.Textarea(attrs={'rows': 12, 'cols': 51, 'placeholder':'Enter your story here',"style":"resize: none;"}))

    class Meta:
            model = Upload
            fields =('__all__')
