# Generated by Django 2.1.1 on 2018-11-16 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classdoor', '0006_classdooruser_profileimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='classdooruser',
            name='reviewsWritten',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='classdoor.Review'),
        ),
    ]
