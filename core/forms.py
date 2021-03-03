from django import forms

from core.models import Resource

class ResourceForm(forms.ModelForm):

    class Meta:
        model = Resource
        fields = (
            'title',
            # 'thumbnail', 
            # 'description',
            'url',
            'category',
            )
        widgets = {
            'category': forms.CheckboxSelectMultiple(),
            # 'description': forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
                'class': 'form-control form-control-sm',
                'placeholder': 'Title',
            })
        # self.fields['description'].widget.attrs.update({
        #         'class': 'form-control form-control-sm',
        #         'placeholder': 'Write a short description',
        #         'rows': 5,
        #     })
        self.fields['url'].widget.attrs.update({
                'class': 'form-control form-control-sm',
                'placeholder': 'Resource URL',
            })
        # self.fields['thumbnail'].widget.attrs.update({
        #         'class': 'form-control-file',
        #         'placeholder': 'Title',
        #     })
        self.fields['category'].widget.attrs.update({
                'class': 'list-inline d-inline-flex flex-wrap',
            })