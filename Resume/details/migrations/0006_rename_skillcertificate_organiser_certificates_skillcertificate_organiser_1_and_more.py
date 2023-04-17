# Generated by Django 4.0.6 on 2023-04-17 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0005_remove_userinfo_skillcertificate_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificates',
            old_name='skillcertificate_organiser',
            new_name='skillcertificate_organiser_1',
        ),
        migrations.RemoveField(
            model_name='certificates',
            name='skillcertificate_link',
        ),
        migrations.RemoveField(
            model_name='certificates',
            name='skillcertificate_logo',
        ),
        migrations.AddField(
            model_name='certificates',
            name='skillcertificate_link_1',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='certificates',
            name='skillcertificate_link_2',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='certificates',
            name='skillcertificate_link_3',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='certificates',
            name='skillcertificate_logo_1',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='certificates',
            name='skillcertificate_logo_2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='certificates',
            name='skillcertificate_logo_3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='certificates',
            name='skillcertificate_organiser_2',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='certificates',
            name='skillcertificate_organiser_3',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
