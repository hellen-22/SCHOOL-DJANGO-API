# Generated by Django 4.0.6 on 2022-10-14 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolDetails', '0004_alter_department_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitdetails',
            name='registration_status',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255),
        ),
    ]
