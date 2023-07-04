# Generated by Django 4.2.2 on 2023-07-04 07:22

from django.db import migrations, models
import paw_prints_app.accounts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images', validators=[paw_prints_app.accounts.validators.validate_file_size]),
        ),
    ]
