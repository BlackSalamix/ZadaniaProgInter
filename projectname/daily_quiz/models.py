from django.db import models
from django.utils import timezone

class Question(models.Model):
    text = models.CharField(max_length=255, verbose_name="Treść pytania")
    used_date = models.DateField(null=True, blank=True, unique=True, verbose_name="Data użycia")
    
    is_approved = models.BooleanField(default=False, verbose_name="Zatwierdzone")
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Pytanie"
        verbose_name_plural = "Pytania"


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    nick = models.CharField(max_length=50, verbose_name="Nick autora")
    content = models.TextField(verbose_name="Treść odpowiedzi")
    
    likes_count = models.IntegerField(default=0, verbose_name="Liczba polubień")
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nick}: {self.content[:30]}..."

    class Meta:
        verbose_name = "Odpowiedź"
        verbose_name_plural = "Odpowiedzi"
        ordering = ['-likes_count']