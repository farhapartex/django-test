# Generated by Django 3.0.3 on 2020-02-25 22:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('survey', '0006_question_survey'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=10, verbose_name='Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qexams', to='survey.Question', verbose_name='Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
