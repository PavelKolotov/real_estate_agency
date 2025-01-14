# Generated by Django 2.2.24 on 2023-03-29 17:54

from django.db import migrations
import phonenumbers


def get_pure_phonenumber(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().iterator():
        pure_phonenumber = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(pure_phonenumber):
            flat.owner_pure_phone = pure_phonenumber
        else:
            flat.owner_pure_phone = None
        flat.save()




class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(get_pure_phonenumber)
    ]
