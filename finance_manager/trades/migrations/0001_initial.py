# Generated by Django 4.2.3 on 2023-08-01 11:32

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
                ('symbol', models.CharField(choices=[('AAPL', 'Apple'), ('GOOG', 'Google'), ('MSFT', 'Microsoft')], max_length=4)),
                ('quantity', models.PositiveIntegerField()),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
