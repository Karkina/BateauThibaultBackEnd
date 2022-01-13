# Generated by Django 3.1.2 on 2022-01-13 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytig', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestIdStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tigID', models.IntegerField(default='-1')),
                ('inStock', models.IntegerField(default='-1')),
            ],
            options={
                'ordering': ('tigID',),
            },
        ),
        migrations.DeleteModel(
            name='TestTableEz',
        ),
    ]
