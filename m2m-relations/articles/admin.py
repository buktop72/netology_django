from django.contrib import admin
from .models import Article, Tag, Relationship
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_counter = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            is_main = form.cleaned_data.get('is_main')
            if is_main:
                is_main_counter += 1
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        if is_main_counter != 1:
            raise ValidationError('Должен быть только один основной раздел!')

        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleInline(admin.TabularInline):
    # model = Article.tag.through
    model = Relationship
    formset = RelationshipInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ArticleInline
    ]
    exclude = ('tag',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [
        ArticleInline
    ]

















# Вместо Object должна быть модель, имеющая связь многие-ко-многим,
# а вместо Relationship должна быть модель связи, указанная как through для связи

# class RelationshipInline(admin.TabularInline):
#     model = Relationship
#
#
# @admin.register(Object)
# class ObjectAdmin(admin.ModelAdmin):
#     inlines = [RelationshipInline]
"""
Однако в этой задаче вам потребуется добавить дополнительную проверку при сохранении объекта. Для этого в объекте Inline'а можно переопределить атрибут formset, который должен указывать на специальный класс типа BaseInlineFormSet, нужный для обработки списка однотипных форм (каждая для своей связи). Воспользуйтесь следующим примером с переопределением метода clean, указанного в качестве formset класса:

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Object, Relationship

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            form.cleaned_data
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
"""