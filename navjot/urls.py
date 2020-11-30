from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index' ),
    path('index-1',views.indexa, name='indexa' ),
    path('index-2',views.indexb, name='indexb' ),
    path('index-3',views.indexc, name='indexc' ),
    path('index-4',views.indexd, name='indexd' )

]
