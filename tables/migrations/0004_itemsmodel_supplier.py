# Generated by Django 4.2 on 2023-05-17 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0003_delete_ordered_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsmodel',
            name='supplier',
            field=models.CharField(max_length=50, null=True),
        ),
    ]