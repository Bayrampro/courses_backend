# Generated by Django 4.2.10 on 2024-08-16 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_is_available'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ('id',), 'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AddField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Название группы'),
        ),
    ]
