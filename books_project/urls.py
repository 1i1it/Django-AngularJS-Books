from django.conf.urls import url

from . import views

app_name = 'books_project'
urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^angular$', views.angular, name='angular'), 
   url(r'^(?P<pk>[0-9]+)$', views.book_detail, name='book_detail'),

]
