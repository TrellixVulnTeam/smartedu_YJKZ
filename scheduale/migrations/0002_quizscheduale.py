# Generated by Django 3.2 on 2022-07-02 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_course_questions'),
        ('module', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scheduale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizScheduale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('due', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.course')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module.module')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
