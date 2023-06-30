# Generated by Django 4.2.2 on 2023-06-29 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('main_characteristics', models.CharField(blank=True, null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='breed_images')),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('pet_category', models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat')], max_length=3)),
                ('age', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('adoption_status', models.CharField(default='Available', max_length=20)),
                ('image', models.ImageField(upload_to='pet_images')),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('breed', models.ForeignKey(blank=True, default='Unknown', null=True, on_delete=django.db.models.deletion.SET_NULL, to='pets.breed')),
            ],
        ),
        migrations.AddField(
            model_name='breed',
            name='related_pets',
            field=models.ManyToManyField(related_name='related_breeds', to='pets.pet'),
        ),
    ]
