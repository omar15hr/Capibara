# Generated by Django 5.0.6 on 2024-06-12 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_orden_direccionentrega_ordenitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('zona', models.CharField(max_length=1)),
            ],
        ),
    ]