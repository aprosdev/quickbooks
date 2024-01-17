# Generated by Django 4.1 on 2022-08-19 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lexulquickbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={},
        ),
        migrations.AddField(
            model_name='customer',
            name='qbd_object_id',
            field=models.CharField(editable=False, max_length=127, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='qbd_object_updated_at',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='qbd_object_version',
            field=models.CharField(editable=False, max_length=127, null=True),
        ),
    ]