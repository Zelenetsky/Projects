# Generated by Django 3.2.4 on 2021-07-04 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoTestTask', '0003_alter_urlstring_url_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlstring',
            name='url_path_test',
            field=models.CharField(default='', max_length=100),
        ),
    ]
