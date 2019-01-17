from django import forms

class Create_Resource_Form(forms.Form):
    name = forms.CharField(label='Name'
        , max_length=100
        , help_text='Enter a unique name for this API')

class Make_Request_Form(forms.Form):
    name = forms.CharField(label='Name'
        , max_length=100
        , help_text='Enter a unique name for this API')

class Permission_Api_Form(forms.Form):
    name = forms.CharField(label='Name'
        , max_length=100
        , help_text='Enter a unique name for this API')
    api_endpoint = forms.CharField(label='API Endpoint'
        , max_length=100
        , help_text='Enter API Endpoint')
    token = forms.CharField(label='API Token'
        , max_length=100
        , help_text='Enter API Token')
    headers = forms.CharField(label='Request Header'
        , widget=forms.Textarea(attrs={'class':'materialize-textarea'})
        , help_text='Enter Content for Request header')
    body = forms.CharField(label='Request Body'
        , widget=forms.Textarea(attrs={'class':'materialize-textarea'})
        , help_text='Enter Content for Request body')
