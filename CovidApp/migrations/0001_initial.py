# Generated by Django 3.1.5 on 2021-02-03 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30)),
                ('Phone', models.CharField(max_length=30)),
                ('Tell', models.CharField(max_length=30)),
            ],
        ),
    ]
