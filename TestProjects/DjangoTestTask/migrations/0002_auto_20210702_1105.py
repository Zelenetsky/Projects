# Generated by Django 3.2.4 on 2021-07-02 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoTestTask', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlString',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_path', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='UrlData',
        ),
    ]