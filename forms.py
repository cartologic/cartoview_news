from django import forms
from news.models import News


class NewsUpdateForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'description', 'image', 'publish_date']
