# Generated by Django 4.1.1 on 2022-09-12 13:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserSimple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TestInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this test instance', primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('acet', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('keto', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('par', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('rpm', models.IntegerField(null=True)),
                ('type', models.CharField(blank=True, max_length=200)),
                ('comment', models.TextField(blank=True, help_text='short comment about test', max_length=1000)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.usersimple')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
