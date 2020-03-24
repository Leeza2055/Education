# Generated by Django 2.2.3 on 2019-07-28 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0003_auto_20190725_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date_of_birth', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('icon', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='facility')),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.CharField(max_length=20),
        ),
    ]
