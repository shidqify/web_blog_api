# Generated by Django 3.2 on 2021-04-28 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('summary', models.TextField(max_length=200)),
                ('body', models.TextField(max_length=5000)),
                ('dateposted', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=50)),
                ('dateupdated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
