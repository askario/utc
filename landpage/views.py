# -*- coding: utf-8 -*- 
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse, Http404
from django.shortcuts import render, render_to_response, redirect
from django.core.paginator import Paginator
from landpage.models import *
from django.contrib import auth
from landpage.forms import CommentForm
from django.core.context_processors import csrf
from django.template.loader import get_template
from django.template import Context


# Create your views here.

def landpage(request):
	args={}
	args['directions']=Direction.objects.all()
	args['lectors']=Lector.objects.all()
	args['clients']=Client.objects.all()
	args['headers'] = Header.objects.all()
	args['username'] = auth.get_user(request).username
	return render_to_response('landpage/index.html',args)


def about(request):
	args={}
	args['abouts']= About.objects.get(id = 1)
	args['approvals'] = Approve.objects.all()
	args['tips'] = ('Лицензии', 'Свидетельства', 'Аттестаты', 'Сертификаты')
	return render_to_response('landpage/about.html', args)


def all_news(request, page_number =1 ):
	news_all = News.objects.all()
	current_page = Paginator(news_all,5)
	args = {}
	args['news'] = current_page.page(page_number)
	args['username']=auth.get_user(request).username
	return render_to_response('landpage/news.html', args)


def news(request, news_id =1):
	comment_form = CommentForm
	args={}
	args.update(csrf(request))
	args['news'] = News.objects.get(id = news_id)
	args['comments'] = Comments.objects.filter(comments_news_id = news_id)
	args['form'] = comment_form
	args['username'] = auth.get_user(request).username
	return render_to_response('landpage/new.html', args)


def addlike(request, news_id):
	try:
		if news_id in request.COOKIES:
			redirect('/')
		else:
			param=News.objects.get(id = news_id)
			param.news_like+=1
			param.save()
			response = redirect('/news/all/#mp1')
			response.set_cookie(news_id, "test")
			return response
	except ObjectDoesNotExists:
		raise Http404
	return redirect('/news/all/#mp1')

def addcomment(request, news_id):
	if request.POST and ("pause" not in request.session):
		form=CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit = False)
			comment.comments_article = News.objects.get(id = news_id)
			form.save()
			request.session.set_expiry(60)
			request.session['pause'] = True
	return redirect('/news/get/%s/' % news_id)
