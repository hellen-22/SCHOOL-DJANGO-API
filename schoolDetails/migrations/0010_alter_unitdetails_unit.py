# Generated by Django 4.0.6 on 2022-10-14 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolDetails', '0009_alter_unitdetails_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitdetails',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='schoolDetails.unit'),
        ),
    ]
