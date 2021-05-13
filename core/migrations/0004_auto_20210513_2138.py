# Generated by Django 3.2.2 on 2021-05-13 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210513_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codesnippet',
            name='embed_code',
        ),
        migrations.AddField(
            model_name='codesnippet',
            name='code',
            field=models.TextField(default='something', verbose_name='Code Snippet'),
            preserve_default=False,
        ),
    ]
