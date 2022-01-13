# Generated by Django 3.1.2 on 2022-01-13 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytig', '0002_auto_20220113_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProduitInSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tigID', models.IntegerField(default='-1')),
            ],
            options={
                'ordering': ('tigID',),
            },
        ),
        migrations.CreateModel(
            name='ProduitStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tigID', models.IntegerField(default='-1')),
                ('inStock', models.IntegerField(default='-1')),
                ('sale', models.IntegerField(default='-1')),
                ('discount', models.FloatField(default='0.0')),
            ],
            options={
                'ordering': ('tigID',),
            },
        ),
        migrations.DeleteModel(
            name='TestIdStock',
        ),
    ]