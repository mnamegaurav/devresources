# Generated by Django 3.2.2 on 2021-05-10 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0019_auto_20210509_2154"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="githubgist",
            name="url",
        ),
        migrations.AddField(
            model_name="githubgist",
            name="embed_code",
            field=models.TextField(
                default="a", verbose_name="GitHub Gist Embed Code with Script Tag"
            ),
            preserve_default=False,
        ),
    ]