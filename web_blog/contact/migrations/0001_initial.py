# Generated by Django 5.0 on 2024-02-07 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='نام')),
                ('email', models.EmailField(max_length=30, verbose_name='ایمیل')),
                ('subject', models.CharField(max_length=30, verbose_name='موضوع')),
                ('company', models.CharField(max_length=30, verbose_name='کمپانی')),
                ('message', models.TextField(verbose_name='پیام')),
            ],
        ),
    ]
