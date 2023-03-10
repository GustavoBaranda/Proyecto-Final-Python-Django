# Generated by Django 4.1.3 on 2022-12-27 02:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='List_of_contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('adress', models.CharField(blank=True, max_length=100)),
                ('mail', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
