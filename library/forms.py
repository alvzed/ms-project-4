from django import forms


class ReviewForm(forms.Form):
    rating = forms.IntegerField(min_value=1, max_value=5,
                                widget=forms.TextInput(attrs={
                                    'type': 'number',
                                    'class': 'number-form-control col-6 col-lg-1'
                                }))
    description = forms.CharField(max_length=512, required=True,
                                  widget=forms.TextInput(attrs={
                                      'placeholder': 'Very smart comment...',
                                      'class': 'form-control col-12 col-md-10 col-lg-8 w-100'
                                  }))
