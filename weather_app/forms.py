from django import forms

class SearchForm(forms.Form):
    search_city = forms.CharField(label='', max_length=100,
                                    widget=forms.TextInput(attrs={'placeholder':'Enter City'}))
    
class AddCity(forms.Form):
    add_city = forms.CharField(label='', max_length=100,
                                    widget=forms.TextInput(attrs={'placeholder':'Add City'}))
    
