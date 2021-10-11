# Generated by Django 3.2.8 on 2021-10-11 06:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userquestion',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='userquestion',
            unique_together={('user', 'question', 'answer')},
        ),
    ]
