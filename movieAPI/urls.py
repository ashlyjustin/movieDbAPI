from django.conf.urls import url


from .import views

from django.urls import path

app_name ='movieAPI'

urlpatterns = [
   
    path('', views.movie_search, name='oxford'),
    path('<movie_id>/<title>',views.movie_data,name='movie_data'),
    
    
]