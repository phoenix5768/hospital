# Generated by Django 4.1.3 on 2022-11-06 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_doctor_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='id_number',
            field=models.BigAutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
