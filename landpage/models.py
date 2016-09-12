# -*- coding: utf-8 -*- 
from django.db import models
from django.utils import timezone


# Create your models here.

class Direction(models.Model):
	class Meta():
		db_table = 'directions'
		verbose_name = 'Направление'
		verbose_name_plural='Направления'

	name = models.CharField(max_length=30, verbose_name='Название направления')
	image = models.CharField(max_length=100, verbose_name='Ссылка на картинку',default = 'http://placehold.it/500x500')
	date = models.DateField( timezone.now())
	text = models.TextField(verbose_name='Описание курса')
	ref_video = models.CharField(max_length=100,verbose_name='Ссылка на видео на youtube.com', default = 'https://youtube.com/')

	def __str__(self):
		return 'Направление %s' % self.name


class Lector(models.Model):
	class Meta():
		db_table = 'lectors'
		verbose_name='Лектор'
		verbose_name_plural='Лекторы'

	name = models.CharField(max_length = 30, verbose_name='Имя лектора')
	surname = models.CharField(max_length = 30, verbose_name = 'Фамилия лектора')
	rang = models.TextField(verbose_name='Должность')
	image = models.CharField(max_length=100, verbose_name='Ссылка на картинку',default = 'http://placehold.it/250x250')



	def __str__(self):
		return 'Лектор %s' % self.name


class Client(models.Model):
	class Meta():
		db_table = 'clients'
		verbose_name='Клиент'
		verbose_name_plural='Клиенты'

	name = models.CharField(max_length =50, verbose_name='Название фирмы-клиента')
	ref = models.CharField(max_length = 50, verbose_name= 'Ссылка на сайт фирмы-клиента', default = '/')
	image = models.CharField(max_length=100,verbose_name = 'Ссылка на лого фирмы-клиента', default = 'http://placehold.it/200x50')

	def __str__(self):
		return 'Клиент %s' % self.name


class Header(models.Model):
	class Meta():
		db_table = 'headers'
		verbose_name='Заголовок'
		verbose_name_plural='Заголовки'

	name = models.CharField(max_length=100,verbose_name='Заголовок')
	image = models.CharField(max_length=100,verbose_name='Иконка', default = 'http://placehold.it/64x64')
	text = models.TextField(verbose_name='Текст заголовка')

	def __str__(self):
		return 'Заголовок %s' % self.name

class About(models.Model):
	class Meta():
		db_table = 'about'
		verbose_name='О компании'

	title = models.CharField(max_length =100, verbose_name='Заголовок')
	text = models.TextField()
	phone= models.CharField(max_length = 20,verbose_name='Телефоны для контактов',default = '+7(347)-xxx-xxx')
	adres = models.CharField(max_length=140, verbose_name='Адрес')

class Approve(models.Model):
	class Meta():
		db_table = 'licence'
		verbose_name = 'Разрещительный документ'
		verbose_name_plural = 'Разрешительные документы'
	
	app_license = 'Лицензии'
	app_svid = 'Свидетельства'
	app_att = 'Аттестаты'
	app_sert = 'Сертификаты'

	app_type = (
		(app_license, 'Лицензии'),
		(app_svid, 'Свидетельства'),
		(app_att, 'Аттестаты'),
		(app_svid, 'Сертификаты')
		)

	name = models.TextField(verbose_name='Описание докумета')
	imp = models.CharField(max_length = 20, verbose_name='Тип документа', choices= app_type)
	ref = models.CharField(max_length=100, verbose_name='Ссылка на изображение', default = 'http://placehold.it/100x100')

	def __str__(self):
		return 'Документ % s' % self.name


class News(models.Model):
	class Meta():
		db_table = 'news'
		verbose_name='Новость'
		verbose_name_plural = 'Новости'
	
	news_title = models.CharField(max_length=30, verbose_name='Заголовок')
	news_text = models.TextField(verbose_name ='Текст новости')
	news_date = models.DateTimeField(timezone.now())
	news_like = models.IntegerField(default = 0)


	def __str__(self):
		return 'Новость %s' % self.news_title


class Comments(models.Model):
	class Meta():
		db_table = 'comments'
		verbose_name='Комментарий'
		verbose_name_plural='Комментарии'

	comments_date = models.DateTimeField(timezone.now())
	comments_text = models.TextField(verbose_name='Текст комментария')
	comments_news = models.ForeignKey(News)
	
