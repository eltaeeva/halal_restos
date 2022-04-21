# Generated by Django 4.0.3 on 2022-04-11 03:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='John(default)', max_length=200, null=True)),
                ('last_name', models.CharField(default='Doe(default)', max_length=200, null=True)),
                ('emaail', models.CharField(default='user@gmail.com', max_length=300, null=True)),
                ('profile_img', models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]