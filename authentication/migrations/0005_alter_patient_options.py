# Generated by Django 4.1.3 on 2022-11-05 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_patient_blood_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name': 'Patient', 'verbose_name_plural': 'Patients'},
        ),
    ]