from django.urls import path
from . import views

urlpatterns = [
    path('', views.site, name='site'),
    path('<int:id>/details/', views.detail, name='details'),
    path('round1/', views.round1, name='round1'),
    path('round2/', views.round2, name='round2'),
    path('round3/', views.round3, name='round3'),
    path('round4/', views.round4, name='round4'),
    path('round5/', views.round5, name='round5'),
    path('round6/', views.round6, name='round6'),
    path('round7/', views.round7, name='round7'),
    path('round8/', views.round8, name='round8'),
    path('round9/', views.round9, name='round9'),
    path('round10/', views.round10, name='round10'),
    path('finish/', views.finish, name='finish'),
]