# Generated by Django 4.0 on 2021-12-19 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('cart', '0003_alter_cart_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.profile'),
        ),
    ]
