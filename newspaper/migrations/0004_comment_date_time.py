# Generated by Django 4.1.1 on 2022-10-19 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0003_alter_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_time',
            field=models.DateTimeField(null=True),
        ),
    ]
