# Generated by Django 4.0.2 on 2022-04-01 18:56

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('cliente', '0003_delete_cliente_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
