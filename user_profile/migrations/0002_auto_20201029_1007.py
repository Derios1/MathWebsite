# Generated by Django 3.1.2 on 2020-10-29 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0004_auto_20201013_2252'),
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='solved_problems',
            field=models.ManyToManyField(to='problems.Problem'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
