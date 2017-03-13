from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django import forms

from .models import News


class NewsCreateForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super(NewsCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.disable_csrf = False
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('title', placeholder="Title"),
            Field('description', placeholder="Description"),
            Field('image'),
            Submit('submit', 'Submit', css_class='btn btn-primary')
        # Submit('submit', 'Submit', css_class='btn btn-primary btn-block')
        )

