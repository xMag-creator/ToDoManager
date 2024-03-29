# Generated by Django 4.0.6 on 2022-07-16 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works_list', '0006_remove_zerolevel_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.RemoveField(
            model_name='fifthlevel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='firstlevel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='fourthlevel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='secondlevel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='thirdlevel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='zerolevel',
            name='description',
        ),
        migrations.AlterField(
            model_name='fifthlevel',
            name='name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='firstlevel',
            name='name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='fourthlevel',
            name='name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='secondlevel',
            name='name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='thirdlevel',
            name='name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='zerolevel',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]
