# Generated by Django 2.1.7 on 2019-03-26 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_movmensalista'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especies', models.CharField(max_length=30)),
            ],
        ),
    ]