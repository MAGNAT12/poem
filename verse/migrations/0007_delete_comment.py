# Generated by Django 4.2.8 on 2025-07-06 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('verse', '0006_remove_comment_content_comment_text_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
