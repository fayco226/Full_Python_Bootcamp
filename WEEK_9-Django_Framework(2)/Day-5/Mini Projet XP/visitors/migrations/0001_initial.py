# Generated by Django 4.1.5 on 2023-01-18 15:26

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bedroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField()),
                ('photo', models.ImageField(default='img_chambre/default.jpg', upload_to='img_chambre')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('avaibility', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bedroom_size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Bedroom_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Simple_Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('review', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitors.visitor')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_update', models.DateField(auto_now=True)),
                ('bedroom', models.ForeignKey(limit_choices_to={'avaibility': True}, on_delete=django.db.models.deletion.CASCADE, to='visitors.bedroom')),
                ('visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitors.visitor')),
            ],
        ),
        migrations.AddField(
            model_name='bedroom',
            name='size_bedroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitors.bedroom_size'),
        ),
        migrations.AddField(
            model_name='bedroom',
            name='type_bedroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitors.bedroom_type'),
        ),
    ]