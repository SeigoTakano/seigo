# Generated by Django 5.1.2 on 2024-11-26 01:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SeigoPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_num', models.CharField(max_length=100, verbose_name='学生番号')),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
                ('subject', models.CharField(max_length=100, verbose_name='科目')),
                ('score', models.CharField(max_length=100, verbose_name='得点')),
                ('datetime', models.DateField(auto_now_add=True, verbose_name='投稿日時')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('score', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seigoapp.student')),
            ],
        ),
    ]
