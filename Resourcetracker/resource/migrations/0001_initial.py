# Generated by Django 3.1.2 on 2021-01-07 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('employee_id', models.CharField(max_length=10)),
                ('email_id', models.EmailField(max_length=254)),
                ('project_name', models.CharField(max_length=30)),
                ('team_name', models.CharField(max_length=30)),
                ('added_on', models.DateField(auto_now=True)),
            ],
        ),
    ]
