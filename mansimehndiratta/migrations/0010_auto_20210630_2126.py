# Generated by Django 2.2 on 2021-06-30 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mansimehndiratta', '0009_auto_20210630_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='title_image',
            field=models.ImageField(null=True, upload_to='mansimehndiratta/images/'),
        ),
    ]