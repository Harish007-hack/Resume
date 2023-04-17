# Generated by Django 4.0.6 on 2023-04-17 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0006_rename_skillcertificate_organiser_certificates_skillcertificate_organiser_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificates',
            old_name='skillcertificate_link_1',
            new_name='skillcertificate_link',
        ),
        migrations.RenameField(
            model_name='certificates',
            old_name='skillcertificate_logo_1',
            new_name='skillcertificate_logo',
        ),
        migrations.RenameField(
            model_name='certificates',
            old_name='skillcertificate_organiser_1',
            new_name='skillcertificate_organiser',
        ),
        migrations.RemoveField(
            model_name='certificates',
            name='skillcertificate_link_2',
        ),
        migrations.RemoveField(
            model_name='certificates',
            name='skillcertificate_link_3',
        ),
        migrations.RemoveField(
            model_name='certificates',
            name='skillcertificate_logo_2',
        ),
        migrations.RemoveField(
            model_name='certificates',
            name='skillcertificate_logo_3',
        ),
        migrations.RemoveField(
            model_name='certificates',
            name='skillcertificate_organiser_2',
        ),
        migrations.RemoveField(
            model_name='certificates',
            name='skillcertificate_organiser_3',
        ),
    ]
