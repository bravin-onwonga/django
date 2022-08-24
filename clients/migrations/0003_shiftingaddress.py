# Generated by Django 3.2.4 on 2022-04-12 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShiftingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.IntegerField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('phonenumber', models.IntegerField(max_length=200, null=True)),
                ('caretaker', models.CharField(max_length=200, null=True)),
                ('streetname', models.CharField(max_length=200, null=True)),
                ('bname', models.CharField(max_length=200, null=True)),
                ('landmark', models.CharField(max_length=200, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.client')),
            ],
        ),
    ]
