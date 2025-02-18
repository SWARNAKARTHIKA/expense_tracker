# Generated by Django 4.0.6 on 2024-07-02 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Et',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_name', models.CharField(blank=True, max_length=20, null=True)),
                ('exp_category', models.CharField(blank=True, max_length=20, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('exp_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'et',
                'managed': False,
            },
        ),
    ]
