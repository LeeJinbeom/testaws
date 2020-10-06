# Generated by Django 3.1.1 on 2020-10-05 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteGroup',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('reg_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TodoGroup',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('del_yn', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=10)),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(blank=True)),
                ('del_yn', models.BooleanField(default=False)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.todogroup')),
            ],
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=100)),
                ('memo', models.TextField()),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.favouritegroup')),
            ],
        ),
    ]
