# Generated by Django 3.1.2 on 2022-01-04 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=50, null=True)),
                ('contact_name', models.CharField(max_length=50, null=True)),
                ('contact_address', models.CharField(max_length=50, null=True)),
                ('category', models.CharField(choices=[('Family', 'Family'), ('Friends', 'Friends'), ('Work', 'Work'), ('Home', 'Home'), ('School', 'School')], max_length=50, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]