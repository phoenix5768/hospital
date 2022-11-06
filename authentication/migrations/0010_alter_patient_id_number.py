# Generated by Django 4.1.3 on 2022-11-06 14:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_patient_id_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='id_number',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]