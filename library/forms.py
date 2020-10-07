from django import forms


class ReviewForm(forms.Form):
    rating = forms.IntegerField(min_value=1, max_value=5,
                                widget=forms.TextInput(attrs={
                                    'type': 'number',
                                    'class': 'mx-2 number-form-control'
                                }))
    description = forms.CharField(max_length=512, required=True,
                                  widget=forms.TextInput(attrs={
                                      'placeholder': 'Very smart comment...',
                                      'class': 'form-control mx-2 w-50'
                                  }))
