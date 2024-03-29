# Generated by Django 4.0.6 on 2022-07-12 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('works_list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256)),
                ('finished', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SecondLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256)),
                ('finished', models.BooleanField(default=False)),
                ('zeroLevel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works_list.firstlevel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='TaskList',
            new_name='ZeroLevel',
        ),
        migrations.CreateModel(
            name='ThirdLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256)),
                ('finished', models.BooleanField(default=False)),
                ('zeroLevel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works_list.secondlevel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FourthLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256)),
                ('finished', models.BooleanField(default=False)),
                ('zeroLevel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works_list.thirdlevel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='firstlevel',
            name='zeroLevel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works_list.zerolevel'),
        ),
        migrations.CreateModel(
            name='FifthLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256)),
                ('finished', models.BooleanField(default=False)),
                ('zeroLevel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works_list.fourthlevel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
