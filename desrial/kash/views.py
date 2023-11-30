from django.shortcuts import render
import io
from .models import Student
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def student_create(request):
    if request.method=='POST':
        json_data=request.body
        stram=io.BytesIO(json_data)
        python_data=JSONParser().parse(stram)
        serial=StudentSerializer(data=python_data)
        if serial.is_valid():
            serial.save()
            msg={'msg':'data insertetd'}
            return HttpResponse(msg)


# Create your views here.
