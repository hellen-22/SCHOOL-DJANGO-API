# Generated by Django 4.0.6 on 2022-10-15 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_lecturer_staff_id_alter_student_reg_no'),
        ('schoolDetails', '0012_alter_unitdetails_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenthostel',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hostel', to='account.student'),
        ),
    ]
