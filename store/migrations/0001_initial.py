# Generated by Django 4.2.8 on 2023-12-14 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to='BannerImage/')),
                ('url_http_link', models.URLField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name_plural': 'Banners',
            },
        ),
    ]