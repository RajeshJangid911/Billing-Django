# Generated by Django 3.1.2 on 2020-10-26 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_invoiceitem_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='challan_nos',
            field=models.CharField(blank=True, default=' ', max_length=150),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
