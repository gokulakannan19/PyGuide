# Generated by Django 3.1.1 on 2020-10-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0005_auto_20201002_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='s_no',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='s_no',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
