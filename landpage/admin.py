from django.contrib import admin
from landpage.models import *

# Register your models here.

class DirectionAdmin(admin.ModelAdmin):
	fields=['name','date','text','ref_video','image']

class LectorAdmin(admin.ModelAdmin):
	fields = ['name', 'surname', 'rang','image']

class ClientAdmin(admin.ModelAdmin):
	fields = ['name','ref','image']

class HeaderAdmin(admin.ModelAdmin):
	fields = [ 'name', 'image', 'text']

class AboutAdmin(admin.ModelAdmin):
	fields = ['title', 'text','phone','adres']

class ApproveAdmin(admin.ModelAdmin):
	fields = ['name', 'imp','ref']

class NewsAdmin(admin.ModelAdmin):
	fields = ['news_title' ,'news_text', 'news_date', 'news_like']

class CommentsAdmin(admin.ModelAdmin):
	fields = ['comments_date','comments_text', 'comments_news']

admin.site.register(Direction, DirectionAdmin)
admin.site.register(Lector, LectorAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Header, HeaderAdmin)
admin.site.register(Approve, ApproveAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentsAdmin)