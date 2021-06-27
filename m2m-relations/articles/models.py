from django.db import models


class Article(models.Model):  # основная таблица
	title = models.CharField(max_length=256, verbose_name='Название')
	text = models.TextField(verbose_name='Текст')
	published_at = models.DateTimeField(verbose_name='Дата публикации')
	image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'

	def __str__(self):
		return self.title


class Scope(models.Model):  # таблица тэгов
	theme = models.TextField(verbose_name='Категория', unique=True)
	articles = models.ManyToManyField(Article, blank=True, related_name='scopes', through='ArticleScope')

	def __str__(self):
		return self.theme

	class Meta:
		verbose_name = 'Тема'
		verbose_name_plural = 'Темы'


class ArticleScope(models.Model):  # промежуточная таблица
	article = models.ForeignKey(Article, related_name='article_theme', on_delete=models.CASCADE)
	theme = models.ForeignKey(Scope, verbose_name='Раздел', related_name='theme_article', on_delete=models.CASCADE)
	main = models.BooleanField(verbose_name='Основной', default=False)

	def __str__(self):
		return f'{self.article} - {self.theme} - {self.main}'

	class Meta:
		verbose_name = 'Тема статьи'
		verbose_name_plural = 'Темы статей'
		ordering = ['-main', 'theme__theme']  # сортировка
