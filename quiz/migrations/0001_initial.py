# Generated by Django 3.1.7 on 2021-03-26 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_cryptography.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('python', django_cryptography.fields.encrypt(models.CharField(max_length=100))),
                ('c', django_cryptography.fields.encrypt(models.CharField(max_length=100))),
                ('java', django_cryptography.fields.encrypt(models.CharField(max_length=100))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]