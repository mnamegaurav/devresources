# Generated by Django 3.2.2 on 2021-05-12 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_squashed_0021_merge_20210511_2217"),
    ]

    operations = [
        migrations.AlterField(
            model_name="githubgist",
            name="embed_code",
            field=models.TextField(
                verbose_name="GitHub Gist Embed Code with Script Tag"
            ),
        ),
    ]