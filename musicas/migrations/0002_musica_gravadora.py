# Generated by Django 4.2.16 on 2024-11-11 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='gravadora',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='musicas.gravadora'),
        ),
    ]
