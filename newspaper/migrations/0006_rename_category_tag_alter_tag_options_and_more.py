# Generated by Django 4.1.1 on 2022-10-04 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0005_remove_article_category_article_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Tag',
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='category',
            new_name='tag',
        ),
    ]