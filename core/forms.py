from django import forms

from core.models import Resource, ContactUs


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
                'placeholder': 'Give it a simple Title...',
            })
        self.fields['url'].widget.attrs.update({
                'class': 'form-control form-control-sm',
                'placeholder': 'Provide a Link...',
            })
        self.fields['category'].widget.attrs.update({
                'class': 'list-inline d-inline-flex flex-wrap m-auto',
            })


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('full_name', 'email', 'message',)
        widgets = {
            'message': forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
                })

            self.fields['full_name'].widget.attrs.update({
                'placeholder': 'Your good name'
                })

            self.fields['email'].widget.attrs.update({
                'placeholder': 'Your email'
                })

            self.fields['message'].widget.attrs.update({
                'placeholder': 'Write something to us...',
                'rows': 3,
                })