# Generated by Django 4.1.5 on 2023-02-21 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_employee_twiter'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='avater',
            field=models.ImageField(null=True, upload_to='Client/Avater'),
        ),
        migrations.AlterField(
            model_name='client',
            name='company_logo',
            field=models.ImageField(null=True, upload_to='Client/Company_Logo'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(null=True)),
                ('reating', models.IntegerField(null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.client')),
            ],
        ),
    ]
