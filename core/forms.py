from django import forms

from core.models import Resource

class ResourceForm(forms.ModelForm):

    class Meta:
        model = Resource
        fields = (
            'title',
            'url',
            'category',
            )
        widgets = {
            # 'category': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
                'class': 'form-control form-control-sm',
                'placeholder': 'Title',
            })
        self.fields['url'].widget.attrs.update({
                'class': 'form-control form-control-sm',
                'placeholder': 'Resource URL',
            })
        self.fields['category'].widget.attrs.update({
                'class': 'list-inline d-inline-flex flex-wrap m-auto',
            })