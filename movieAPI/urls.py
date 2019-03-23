from django.conf.urls import url


from .import views

from django.urls import path

app_name ='movieAPI'

urlpatterns = [
   
    path('movie/', views.oxford, name='oxford'),
    path('movie/<movie_id>/<title>',views.movie_data,name='movie_data'),
    
    
]