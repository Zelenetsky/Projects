# Generated by Django 3.2.4 on 2021-07-05 13:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoTestTask', '0005_remove_urlstring_url_path_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlstring',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]