from django import forms

from core.models import Resource, GitHubGist, ContactUs


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = (
            "title",
            "url",
            "category",
        )
        widgets = {
            # 'category': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update(
            {
                "class": "form-control form-control-sm",
                "placeholder": "Give it a simple Title...",
            }
        )
        self.fields["url"].widget.attrs.update(
            {
                "class": "form-control form-control-sm",
                "placeholder": "Provide a Link...",
            }
        )
        self.fields["category"].widget.attrs.update(
            {
                "class": "list-inline d-inline-flex flex-wrap m-auto",
            }
        )


class GitHubGistForm(forms.ModelForm):
    class Meta:
        model = GitHubGist
        fields = (
            "title",
            "embed_code",
            "category",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update(
            {
                "class": "form-control form-control-sm",
                "placeholder": "Give it a simple Title...",
            }
        )
        self.fields["embed_code"].widget.attrs.update(
            {
                "class": "form-control form-control-sm",
                "placeholder": f"Please write a valid Embed code of a Github Gist, something like this:-\n<script src='https://gist.github.com/username/751dd0fe34a6a8f9ec1597a96e4a665f.js'></script>",
            }
        )
        self.fields["category"].widget.attrs.update(
            {
                "class": "list-inline d-inline-flex flex-wrap m-auto",
            }
        )


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            "full_name",
            "email",
            "message",
        )
        widgets = {
            "message": forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

            self.fields["full_name"].widget.attrs.update(
                {"placeholder": "Your good name"}
            )

            self.fields["email"].widget.attrs.update({"placeholder": "Your email"})

            self.fields["message"].widget.attrs.update(
                {
                    "placeholder": "Write something to us...",
                    "rows": 3,
                }
            )
