from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.template import loader

def my_app(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
def test(request):
  return render(request,'test.html')