# Generated by Django 5.1 on 2024-09-23 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0002_alter_expense_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='created_date',
            field=models.DateTimeField(auto_now=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='expense',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
