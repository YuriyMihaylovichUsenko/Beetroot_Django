# Generated by Django 4.1.1 on 2022-10-05 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0016_rename_da_news_article_date_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='date_news',
        ),
    ]
