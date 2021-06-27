from django.contrib import admin
from django.core.exceptions import ValidationError  # Проверка форм и полей формы
from django.forms import BaseInlineFormSet  #  вложенные формы
from .models import Article, Scope, ArticleScope


class ArticleScopeInlineFormset(BaseInlineFormSet):
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


class ArticleScopeInline(admin.TabularInline):
	model = ArticleScope
	extra = 1


class ArticleAdmin(admin.ModelAdmin):
	inlines = (ArticleScopeInline,)


class ScopeAdmin(admin.ModelAdmin):
	inlines = (ArticleScopeInline,)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Scope, ScopeAdmin)
