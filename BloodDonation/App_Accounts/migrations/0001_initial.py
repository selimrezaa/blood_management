# Generated by Django 3.2.7 on 2021-09-27 13:57

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
            name='BloodGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('permanent', 'Permanent'), ('blood doner', 'Blood Doner'), ('money doner', 'MOney Doner')], max_length=20)),
                ('phone', models.CharField(blank=True, max_length=11)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('facebook', models.CharField(blank=True, max_length=100)),
                ('twitter', models.CharField(blank=True, max_length=100)),
                ('instragam', models.CharField(blank=True, max_length=100)),
                ('linkedin', models.CharField(blank=True, max_length=100)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=30)),
                ('religion', models.CharField(blank=True, choices=[('muslim', 'Muslim'), ('hinduism', 'Hinduism'), ('buddhism', 'Buddhism'), ('christianity', 'Christianity')], max_length=20)),
                ('totaldonate', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Profile')),
                ('dob', models.DateField()),
                ('lastdonate', models.DateField()),
                ('aboutyou', models.TextField()),
                ('bloodgroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Accounts.bloodgroup')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
