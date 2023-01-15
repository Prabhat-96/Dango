from django.contrib import admin
from django.urls import path
from django.urls import include, path

urlpatterns = [
    path('', include('my_app.urls')),
    path('admin/', admin.site.urls),
    path('signin',include('my_app.urls')),
    path('forgot',include('my_app.urls')),
    path('home',include('my_app.urls')),
    path('signup',include('my_app.urls')),
    path('login',include('my_app.urls')),
<<<<<<< HEAD
    path('test',include('my_app.urls')),
=======
    path('Languages',include('my_app.urls')),
    path('Levels',include('my_app.urls')),
>>>>>>> fcd19046ca084faa470eaaa2cd30b376ab3a0506
]
