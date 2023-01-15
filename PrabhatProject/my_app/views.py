from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
# from .models import users
import mysql.connector
email=''
fullname=''
password=''
email2=''
password2=''
testing=''
def my_app(request):
  return render(request,'index.html')

def signin(request):
  return render(request,'signin.html')

def login(request):
  global email2,password2
  if request.method=='POST':
      mydb=mysql.connector.connect(host="localhost",user="root",passwd="password",database="programmerji")
      mycursor=mydb.cursor()
      d=request.POST
      for key,value in d.items():
          if key=="email2":
            email2=value
          if key=="password2":
              password2=value
      c="select exists(select * from users where email='"+email2+"')"
      mycursor.execute(c)
      for k in mycursor:
          for f in k:
              if f==0:
                messages.success(request,"Incorrect email")
      m="select password from users where email='"+email2+"'"
      mycursor.execute(m)
      for x in mycursor:
        b=''
        for j in x:
          b+=j
          if b==password2:
            messages.success(request,"you have successfully logged in!!")
          else:
            messages.success(request,"Incorrect password!!")
      return render(request,'signin.html')
def signup(request):
  if request.method=='POST':
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="password",database="programmerji")
        mycursor=mydb.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                email=value
            if key=="fullname":
                fullname=value
            if key=="password":
                password=value
        c="insert into users values('{}','{}','{}')".format(email,fullname,password)
        mycursor.execute(c)
        mydb.commit()
        return render(request,'signin.html')

def forgot(request):
  return render(request,'forgot.html')

def test(request):
  return render(request,"test.html")