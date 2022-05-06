from django.db import models

class Direction(models.Model):
    title = models.CharField(max_length=100)
    position = models.IntegerField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Направления'
        verbose_name_plural = 'Направлении'


class LessonMaterial(models.Model):
    title = models.CharField(max_length=100)
    material1 = models.TextField()
    material2 = models.TextField()
    material3 = models.TextField()
    material4 = models.TextField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    position = models.IntegerField()
    anons = models.CharField(max_length=255)
    description = models.TextField()
    link_to_video = models.URLField(verbose_name='Ссылка')
    link_to_file = models.URLField(verbose_name='Ссылка')
    materials = models.ManyToManyField(LessonMaterial, verbose_name='Материалы')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Course(models.Model):
    title = models.CharField(max_length=100)
    position = models.IntegerField()
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    lessons = models.ManyToManyField(Lesson, verbose_name='Уроки')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
