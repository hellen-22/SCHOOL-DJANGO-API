# Generated by Django 4.0.6 on 2022-10-14 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolDetails', '0006_alter_unitdetails_registration_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitdetails',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='schoolDetails.unit', unique=True),
        ),
    ]