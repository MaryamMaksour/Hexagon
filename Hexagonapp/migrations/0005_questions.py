# Generated by Django 5.0.3 on 2024-03-19 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hexagonapp', '0004_alter_project_industry_sector_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]