# Generated by Django 3.2.5 on 2022-01-22 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, unique=True)),
                ('content', models.TextField()),
                ('question1', models.CharField(choices=[('1', 'Yes'), ('2', 'No'), ('3', 'Mabye')], max_length=40)),
            ],
        ),
    ]