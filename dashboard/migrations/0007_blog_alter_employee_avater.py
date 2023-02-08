# Generated by Django 4.1.5 on 2023-02-06 01:32

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_project_full_capture_alter_client_company_logo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('cover_image', models.ImageField(null=True, upload_to='Blog/Cover')),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='avater',
            field=models.ImageField(null=True, upload_to='Employee/Avater'),
        ),
    ]
