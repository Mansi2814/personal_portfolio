# Generated by Django 2.2 on 2021-06-30 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mansimehndiratta', '0011_auto_20210630_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title_img_upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_upload', models.ImageField(null=True, upload_to='mansimehndiratta/images')),
            ],
        ),
        migrations.RemoveField(
            model_name='blogs',
            name='title_image',
        ),
    ]