
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Treść pytania')),
                ('used_date', models.DateField(blank=True, null=True, unique=True, verbose_name='Data użycia')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Zatwierdzone')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Pytanie',
                'verbose_name_plural': 'Pytania',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=50, verbose_name='Nick autora')),
                ('content', models.TextField(verbose_name='Treść odpowiedzi')),
                ('likes_count', models.IntegerField(default=0, verbose_name='Liczba polubień')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='daily_quiz.question')),
            ],
            options={
                'verbose_name': 'Odpowiedź',
                'verbose_name_plural': 'Odpowiedzi',
                'ordering': ['-likes_count'],
            },
        ),
    ]
