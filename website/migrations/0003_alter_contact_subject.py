# Generated by Django 3.2.18 on 2023-04-23 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, default=1, max_length=255),
            preserve_default=False,
        ),
    ]
