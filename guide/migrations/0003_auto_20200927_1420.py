# Generated by Django 3.1.1 on 2020-09-27 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0002_auto_20200927_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='purpose',
            field=models.CharField(choices=[('get_answer', 'get_answer'), ('submit_answer', 'submit_answer')], default=True, max_length=30),
        ),
    ]
