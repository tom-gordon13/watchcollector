# Generated by Django 4.0.3 on 2022-05-12 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_component_alter_servicing_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='components',
            field=models.ManyToManyField(to='main_app.component'),
        ),
    ]
