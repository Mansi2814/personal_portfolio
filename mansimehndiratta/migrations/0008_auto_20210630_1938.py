# Generated by Django 2.2 on 2021-06-30 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mansimehndiratta', '0007_remove_blogs_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='title_image',
            field=models.ImageField(null=True, upload_to='mansimehndiratta/images'),
        ),
    ]
