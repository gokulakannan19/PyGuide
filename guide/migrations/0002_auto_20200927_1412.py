# Generated by Django 3.1.1 on 2020-09-27 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='purpose',
            field=models.CharField(choices=[('submit_answer', 'submit_answer'), ('get_answer', 'get_answer')], default=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(default=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
