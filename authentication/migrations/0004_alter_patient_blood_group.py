# Generated by Django 4.1.3 on 2022-11-05 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_patient_martial_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='blood_group',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('O', 'O'), ('AB', 'AB')], max_length=5, verbose_name='Blood group'),
        ),
    ]
