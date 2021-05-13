# Generated by Django 3.1.7 on 2021-03-02 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_resourcecategory_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resourcecategory',
            options={'ordering': ['title'], 'verbose_name': 'Resource Category', 'verbose_name_plural': 'Resource Categories'},
        ),
        migrations.AlterField(
            model_name='resourcecategory',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]