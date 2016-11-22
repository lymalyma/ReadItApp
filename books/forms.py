from django import forms

class ReviewForm(forms.Form):
    """
    Form for reviewing a book
    """
    is_favourite = forms.BooleanField(
        label='Favourites',
        help_text='In your top 100 fave books',
        required=False, # in our form, this will not be required
    )

    review = forms.CharField(
        widget = forms.Textarea,
        min_length = 300,
        error_messages = {
            'required': 'Please enter your review',
            'min_lenght': 'Please write at least 300 chararacters. (You have written %(show_value)s)'
        },
    )
