# Generated by Django 4.0.6 on 2022-07-16 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works_list', '0007_delete_test_remove_fifthlevel_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('finished', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
