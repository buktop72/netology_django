from django.db import models


class Student(models.Model):

    name = models.TextField()

    birth_date = models.DateField(
        null=True,
    )

    def __str__(self):
        return f'{self.name}  - {self.birth_date}'

    class Meta:  # отображение моделей в админке
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Course(models.Model):

    name = models.TextField()

    students = models.ManyToManyField(
        Student,
        blank=True,
    )

    def __str__(self):
        return f'{self.name}  - {self.students}'

    class Meta:  # отображение моделей в админке
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
