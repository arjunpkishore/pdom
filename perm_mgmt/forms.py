from django import forms

class Create_Resource_Form(forms.Form):
    name = forms.CharField(label='Name'
        , max_length=100
        , help_text='Enter a unique name for this Resource')
    description = forms.CharField(label='Description'
        , widget=forms.Textarea(attrs={'class':'materialize-textarea'})
        , help_text='Enter a description for the resource')
    p_resource = forms.CharField(label='Parent Resource'
        , max_length=100
        , help_text='Enter a Parent resource. Leave blank if this is a ROOT resource')
    approver = forms.CharField(label='Approver'
        , max_length=100
        , help_text='Enter cdsid of approver. Separate multiple approvers with commas')
    p_api = forms.CharField(label='API for granting permission'
        , max_length=100
        , help_text='Select API to be invoked for granting access')

class Make_Request_Form(forms.Form):
    target = forms.CharField(label='Resource'
        , max_length=100
        , help_text='Select a resource for which access is being requested')
    fim = forms.CharField(label='FIM group'
        , max_length=100
        , help_text='Enter a FIM group to which access has to be added')


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
