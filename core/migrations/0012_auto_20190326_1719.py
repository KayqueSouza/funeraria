# Generated by Django 2.1.7 on 2019-03-26 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190326_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='alimentacao',
            name='Cristo',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alimentacao',
            name='biblia',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alimentacao',
            name='cpf_fal',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alimentacao',
            name='os',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alimentacao',
            name='remocao',
            field=models.ForeignKey(default=1, on_delete='', to='core.LocalRemocao'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alimentacao',
            name='sem_adereco',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alimentacao',
            name='urna',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alimentacao',
            name='veu',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
