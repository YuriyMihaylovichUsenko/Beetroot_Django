# Generated by Django 4.1.1 on 2022-10-05 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0015_rename_date_news_article_da_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='da_news',
            new_name='date_news',
        ),
    ]