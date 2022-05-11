# Generated by Django 4.0.3 on 2022-05-11 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('cost', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[('G', 'General Maintenance'), ('R', 'Mechanical Repairs'), ('S', 'Strap Replacement')], default='G', max_length=1)),
                ('watch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.watch')),
            ],
        ),
    ]