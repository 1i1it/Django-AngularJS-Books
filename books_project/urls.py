# from django.conf.urls import url

# from . import views

# app_name = 'books_project'
# urlpatterns = [
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
# ]



from django.conf.urls import url

from . import views

app_name = 'books_project'
urlpatterns = [
   url(r'^$', views.index, name='index'),
   
   url(r'^angular$', views.angular, name='angular'), 
   url(r'^(?P<pk>[0-9]+)$', views.book_detail, name='book_detail'), # 1. do a get request to read data


    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]


# 2. a post request to insert data,
# 3. an put request to update data and a
# 4 delete request to delete data) 