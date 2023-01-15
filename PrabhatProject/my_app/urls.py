from django.urls import path
from .import views

urlpatterns = [
    path('', views.my_app, name='my_app'),
    path('my_app/', views.my_app, name='my_app'),
    path('signin',views.signin),
    path('forgot',views.forgot),
    path('home',views.my_app),
    path('signup',views.signup),
    path('login',views.signin),
<<<<<<< HEAD
    path('test',views.test),
]
=======
    path('Languages',views.Languages),
    path('Levels',views.Levels)
    ]
>>>>>>> fcd19046ca084faa470eaaa2cd30b376ab3a0506
