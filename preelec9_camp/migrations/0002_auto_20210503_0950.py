# Generated by Django 3.1.7 on 2021-05-03 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preelec9_camp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campdata',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='campdata',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='campdata',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='campdata',
            name='nickname',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='campdata',
            name='self_telephone_num',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
