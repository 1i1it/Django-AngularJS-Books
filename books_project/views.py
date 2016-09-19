from django.shortcuts import render
from .models import Book
from django.core import serializers
import json
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pdb
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
from django.http import HttpResponse
from django.template import loader


@csrf_exempt
def index(request):
	if request.method == 'GET':
		data = serializers.serialize('json', Book.objects.all())
		data = json.loads(data)
		#data = {"data": data}
		return JsonResponse(data, safe=False)

	elif request.method == 'POST':
		params = json.loads(request.body)
		book = Book.objects.create(title=params['title'], description=params['description'], author_id=1)
		data = serializers.serialize('json', [book])
		data = json.loads(data)[0]
		return JsonResponse(data, safe=False)


@csrf_exempt
def book_detail(request, pk):
	if request.method == 'GET':
		try:
			book = Book.objects.get(pk=pk)
			data = serializers.serialize('json', [book])
			data = json.loads(data)[0]
		except Book.DoesNotExist:
			data = {"error":"book not found"}
		return JsonResponse(data, safe=False)
	
	elif request.method == 'PUT':
		params = json.loads(request.body)
		title=params['title']
		description=params['description']

		Book.objects.filter(pk=pk).update(title=title, description=description)
		book = Book.objects.get(pk=pk)


		data = serializers.serialize('json', [book])
		data = json.loads(data)[0]
		return JsonResponse(data, safe=False)
	elif request.method == 'DELETE':
		book = Book.objects.get(pk=pk)
		book.delete()
		data = {"success":"book deleted"}
		return JsonResponse(data, safe=False)

def angular(request):
	template = loader.get_template('books_project/index.html')
	template_name = 'index.html'
	context = {
        'latest_question_list': "latest_question_list",
    }
	return HttpResponse(template.render(context, request))