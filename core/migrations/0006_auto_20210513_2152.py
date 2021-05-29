# Generated by Django 3.2.2 on 2021-05-13 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_codesnippet_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcecategory',
            name='is_programming_language',
            field=models.BooleanField(default=True, verbose_name='Programming Language?'),
        ),
        migrations.AlterField(
            model_name='codesnippet',
            name='code',
            field=models.TextField(verbose_name='Code Snippet'),
        ),
    ]