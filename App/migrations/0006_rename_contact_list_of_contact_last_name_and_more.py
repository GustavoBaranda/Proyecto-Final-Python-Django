# Generated by Django 4.1.3 on 2023-01-02 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_remove_profile_user_mail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list_of_contact',
            old_name='contact',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='list_of_contact',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
