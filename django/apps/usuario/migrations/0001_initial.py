# Generated by Django 2.1.3 on 2019-04-11 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario_nome', models.CharField(max_length=100)),
                ('usuario_cpf', models.CharField(max_length=14)),
                ('usuario_rg', models.CharField(max_length=30)),
                ('usuario_cep', models.CharField(max_length=11)),
                ('usuario_profissao', models.CharField(max_length=20)),
                ('usuario_estado_civil', models.CharField(choices=[('solteiro', 'Solteiro(a)'), ('casado', 'Casado(a)'), ('divorciado', 'Divorciado(a)'), ('viuvo', 'Viúvo(a)')], max_length=20)),
                ('usuario_rua', models.CharField(max_length=50)),
                ('usuario_bairro', models.CharField(max_length=20)),
                ('usuario_cidade', models.CharField(max_length=20)),
                ('usuario_email', models.EmailField(max_length=254)),
                ('usuario_telefone', models.CharField(max_length=20)),
                ('usuario_celular', models.CharField(max_length=20)),
                ('usuario_site', models.CharField(max_length=30)),
            ],
        ),
    ]
