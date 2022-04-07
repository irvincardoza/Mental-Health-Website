from django.urls import path
from inno_app import views

urlpatterns=[
        path('',views.index, name='index'),
        path('contact/',views.contact,name='contact'),
        path('display/',views.display, name='display'),
        path('article1/',views.article1,name='article1'),
        path('article2/',views.article2,name='article2'),
        path('article3/',views.article3,name='article3'),
        path('article4/',views.article4,name='article4'),
        path('article5/',views.article5,name='article5'),
        path('story/',views.story,name='story'),
        path('info/',views.info,name='info'),
        path('upload/',views.upload,name='upload'),
        path('storypage/',views.storypage,name='storypage'),
        path('videopage/',views.videopage,name='videopage')


]
