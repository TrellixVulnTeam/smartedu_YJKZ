# Generated by Django 3.2 on 2022-07-04 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizai', '0001_initial'),
        ('module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='quizzes_ai',
            field=models.ManyToManyField(to='quizai.QuizzesAI'),
        ),
    ]
