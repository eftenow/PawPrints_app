# Generated by Django 4.2.5 on 2023-10-08 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0009_remove_pet_adopted_by_remove_pet_breed_pet_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='town',
            field=models.CharField(default='Sofia'),
        ),
    ]