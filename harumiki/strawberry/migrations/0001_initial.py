# Generated by Django 5.1.1 on 2024-09-06 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('water_ph', models.FloatField(blank=True, null=True)),
                ('water_ec', models.FloatField(blank=True, null=True)),
                ('z1_ph1', models.FloatField(blank=True, null=True)),
                ('z1_ph2', models.FloatField(blank=True, null=True)),
                ('z1_ec1', models.FloatField(blank=True, null=True)),
                ('z1_ec2', models.FloatField(blank=True, null=True)),
                ('z1_ml', models.FloatField(blank=True, null=True)),
                ('z1_rh', models.FloatField(blank=True, null=True)),
                ('z2_ph1', models.FloatField(blank=True, null=True)),
                ('z2_ph2', models.FloatField(blank=True, null=True)),
                ('z2_ec1', models.FloatField(blank=True, null=True)),
                ('z2_ec2', models.FloatField(blank=True, null=True)),
                ('z2_ml', models.FloatField(blank=True, null=True)),
                ('z2_rh', models.FloatField(blank=True, null=True)),
                ('z3_ph1', models.FloatField(blank=True, null=True)),
                ('z3_ph2', models.FloatField(blank=True, null=True)),
                ('z3_ec1', models.FloatField(blank=True, null=True)),
                ('z3_ec2', models.FloatField(blank=True, null=True)),
                ('z3_ml', models.FloatField(blank=True, null=True)),
                ('z3_rh', models.FloatField(blank=True, null=True)),
                ('z4_ph1', models.FloatField(blank=True, null=True)),
                ('z4_ph2', models.FloatField(blank=True, null=True)),
                ('z4_ec1', models.FloatField(blank=True, null=True)),
                ('z4_ec2', models.FloatField(blank=True, null=True)),
                ('z4_ml', models.FloatField(blank=True, null=True)),
                ('z4_rh', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
