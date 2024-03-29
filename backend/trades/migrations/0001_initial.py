# Generated by Django 4.2.3 on 2023-08-19 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('quantity', models.PositiveIntegerField()),
                ('purchase_price', models.DecimalField(decimal_places=3, max_digits=18)),
                ('current_price', models.DecimalField(decimal_places=3, max_digits=18, null=True)),
                ('type', models.CharField(max_length=4, null=True)),
                ('time', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
