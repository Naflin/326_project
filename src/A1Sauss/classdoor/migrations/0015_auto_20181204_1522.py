# Generated by Django 2.1.2 on 2018-12-04 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classdoor', '0014_auto_20181204_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='reviews',
            field=models.ForeignKey(help_text='Select a tag for this tag', null=True, on_delete=django.db.models.deletion.SET_NULL, to='classdoor.Review'),
        ),
    ]
