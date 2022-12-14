# Generated by Django 4.1.3 on 2022-12-05 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_userr_expiry_remove_userr_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('sold', models.BooleanField(default=False)),
                ('itemId', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Emails',
        ),
        migrations.DeleteModel(
            name='Proxies',
        ),
    ]
