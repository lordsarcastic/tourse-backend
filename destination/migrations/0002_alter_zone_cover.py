# Generated by Django 3.2.10 on 2022-01-31 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0011_auto_20190223_2138'),
        ('destination', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zone',
            name='cover',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photologue.photo'),
        ),
    ]