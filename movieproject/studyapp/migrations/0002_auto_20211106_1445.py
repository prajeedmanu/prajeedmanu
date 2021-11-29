# Generated by Django 3.2.8 on 2021-11-06 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='inmakesproject')),
                ('desc', models.TextField()),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='person',
        ),
        migrations.DeleteModel(
            name='place',
        ),
    ]
