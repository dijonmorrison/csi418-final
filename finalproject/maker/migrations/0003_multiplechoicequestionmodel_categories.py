# Generated by Django 2.1.7 on 2019-03-25 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maker', '0002_auto_20190325_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='multiplechoicequestionmodel',
            name='categories',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='maker.QuestionCategory'),
        ),
    ]
