from django import forms


class ReviewForm(forms.Form):
    user = forms.CharField(max_length=254, required=True,
                           widget=forms.TextInput(attrs={
                               'type': 'hidden'
                           }))
    nickname = forms.CharField(max_length=254, required=True,
                               widget=forms.TextInput(attrs={
                                   'type': 'hidden'
                               }))
    rating = forms.IntegerField(min_value=1, max_value=5)
    description = forms.CharField(max_length=512, required=True,
                                  widget=forms.TextInput(attrs={
                                      'placeholder': 'Very smart comment...'
                                  }))
