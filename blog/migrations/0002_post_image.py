# Generated by Django 2.2.17 on 2020-11-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='none', upload_to='images/'),
            preserve_default=False,
        ),
    ]
