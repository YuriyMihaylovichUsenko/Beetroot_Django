# Generated by Django 4.1.1 on 2022-10-05 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0010_alter_article_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='date',
        ),
    ]