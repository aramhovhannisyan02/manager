# Generated by Django 4.2 on 2023-05-18 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0007_remove_itemsmodel_customer_itemsmodel_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemsmodel',
            name='customer',
        ),
        migrations.AddField(
            model_name='itemsmodel',
            name='customer',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
