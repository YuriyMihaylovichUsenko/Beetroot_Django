# Generated by Django 4.1.1 on 2022-10-05 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0018_remove_article_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
    ]