# Generated by Django 4.2.13 on 2024-06-07 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mytable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodect_name', models.CharField(max_length=30, null=True)),
                ('prodect_code', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
