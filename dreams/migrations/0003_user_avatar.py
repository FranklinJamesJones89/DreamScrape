# Generated by Django 4.1.7 on 2023-03-01 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreams', '0002_user_bio_user_name_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar.svg', null=True, upload_to=''),
        ),
    ]
