# Generated by Django 3.2.5 on 2022-01-23 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inno_app', '0003_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='question1',
            field=models.CharField(choices=[('1', 'Yes'), ('2', 'No'), ('3', 'Mabye')], max_length=40, null=True),
        ),
    ]
