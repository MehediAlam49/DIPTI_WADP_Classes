# Generated by Django 5.2.3 on 2025-06-25 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('author', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('published_date', models.DateField(null=True)),
            ],
        ),
    ]
