# Generated by Django 3.2.8 on 2021-10-26 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0003_auto_20211026_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.group'),
        ),
    ]
