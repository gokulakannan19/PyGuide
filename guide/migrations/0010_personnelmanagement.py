# Generated by Django 3.1.1 on 2020-10-05 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0009_corporateaccounting'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonnelManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.PositiveIntegerField(null=True)),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
