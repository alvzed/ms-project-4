from django import forms


class ReviewForm(forms.Form):
    rating = forms.IntegerField(min_value=1, max_value=5)
    description = forms.CharField(max_length=512, required=True,
                                  widget=forms.TextInput(attrs={
                                      'placeholder': 'Very smart comment...'
                                  }))
