# Generated by Django 3.2.5 on 2022-07-16 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
