# Generated by Django 4.0 on 2022-04-23 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_table_floor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='Floor',
        ),
        migrations.AddField(
            model_name='table',
            name='floor',
            field=models.CharField(choices=[('Ground', 'Ground'), ('First', 'First'), ('Second', 'Second'), ('Fourth', 'Fourth'), ('RoofTop', 'RoofTop')], max_length=50, null=True),
        ),
    ]
