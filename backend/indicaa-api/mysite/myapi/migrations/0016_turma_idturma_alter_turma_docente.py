# Generated by Django 4.0.3 on 2022-03-31 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0015_alter_turma_ano_alter_turma_semestre'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='idTurma',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='turma',
            name='docente',
            field=models.CharField(max_length=255),
        ),
    ]
