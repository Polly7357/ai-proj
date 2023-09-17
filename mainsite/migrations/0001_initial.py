# Generated by Django 4.1 on 2023-09-17 08:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beverage',
            fields=[
                ('id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('cde', models.FloatField(blank=True)),
                ('unit', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'beverage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='C2Rates',
            fields=[
                ('h_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'c2_rates',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='C3Rates',
            fields=[
                ('h_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'c3_rates',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CdeTransport',
            fields=[
                ('id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('cde', models.FloatField(blank=True)),
                ('unit', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'cde_transport',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CfpClass',
            fields=[
                ('class_id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('class_name', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'cfp_class',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CfpSosClass',
            fields=[
                ('cfp_sos_class_id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('cfp_sos_class_name', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'cfp_sos_class',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CfpSubClass',
            fields=[
                ('sub_class_id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('sub_class_name', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'cfp_sub_class',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EggProds',
            fields=[
                ('id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('cde', models.FloatField(blank=True)),
                ('unit', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'egg_prods',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ElecDeviceConsumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
                ('watt', models.IntegerField(blank=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'elec_device_consumption',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Energy',
            fields=[
                ('id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('cde', models.FloatField(blank=True)),
                ('unit', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'energy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LactoseProds',
            fields=[
                ('id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('cde', models.FloatField(blank=True)),
                ('unit', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'lactose_prods',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SummerC2Rates',
            fields=[
                ('h_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'summer_c2_rates',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SummerC3Rates',
            fields=[
                ('h_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'summer_c3_rates',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TimeElecRates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('effect_date', models.IntegerField()),
                ('rates', models.FloatField(blank=True)),
            ],
            options={
                'db_table': 'time_elec_rates',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='SmartPlugRec',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timestmp', models.DateTimeField(unique=True)),
                ('response', models.JSONField()),
            ],
            options={
                'db_table': 'plug_info',
                'ordering': ['-timestmp'],
            },
        ),
    ]
