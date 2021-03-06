# Generated by Django 4.0.5 on 2022-06-19 10:44

import cloudinary.models
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
            name='NeighborHood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hood_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=200, null=True)),
                ('health_contact', models.IntegerField(blank=True, null=True)),
                ('police_contact', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=250)),
                ('avatar', cloudinary.models.CloudinaryField(max_length=255, verbose_name='images')),
                ('neighborhood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Neighbor.neighborhood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Neighbor.neighborhood')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood', to='Neighbor.userprofile'),
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business', to='Neighbor.neighborhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='Neighbor.userprofile')),
            ],
        ),
    ]
