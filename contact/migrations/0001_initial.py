# Generated by Django 3.2.14 on 2022-07-26 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('artist', models.CharField(choices=[('becky', 'Becky Johnson'), ('alex', 'Alex Anderson'), ('john', 'John Masters'), ('alison', 'Alison Taylor'), ('jasmine', 'Jasmine Evans'), ('david', 'David Walker'), ('any', 'Any')], default='any', max_length=20)),
                ('subject', models.CharField(choices=[('consultation', 'Free Consultation'), ('new', 'New Inquiry'), ('reschedule', 'Reschedule Appointment'), ('aftercare', 'Aftercare Inquiry'), ('other', 'Other')], default='other', max_length=13)),
                ('requested_date', models.DateField()),
                ('message', models.TextField()),
                ('sent', models.DateTimeField(auto_now_add=True)),
                ('replied', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=80)),
                ('body', models.TextField()),
                ('sent', models.DateTimeField(auto_now_add=True)),
                ('replied', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('artist', models.CharField(choices=[('becky', 'Becky Johnson'), ('alex', 'Alex Anderson'), ('john', 'John Masters'), ('alison', 'Alison Taylor'), ('jasmine', 'Jasmine Evans'), ('david', 'David Walker'), ('any', 'Any')], default='any', max_length=20)),
                ('body', models.TextField(max_length=250)),
                ('sent', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
    ]
