from django.db import models

class Author(models.Model):
    name = models.CharField("Имя автора", max_length=100)
    bio = models.TextField("Биография", blank=True)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    PART_CHOICES = [
        (1, 'Часть 1'),
        (2, 'Часть 2'),
    ]
    
    title = models.CharField("Заголовок", max_length=200)
    part = models.PositiveSmallIntegerField("Часть", choices=PART_CHOICES)
    content = models.TextField("Содержание")
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    
    def __str__(self):
        return f"{self.title} - {self.get_part_display()}"