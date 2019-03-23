
from django.shortcuts import render
from .forms import DictionaryForm
from decouple import config
import requests
from django.http import HttpResponse
import datetime
MovieDB_KEY = config('MovieDB_APP_Key')


def oxford(request):
    search_result = {}
    if 'movie' in request.GET:
        form = DictionaryForm(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = DictionaryForm()
    return render(request, 'movieSearch/search.html', {'form': form, 'search_result': search_result})

def movie_data(request,movie_id,title):
        result = {}
    
        endpoint = 'https://api.themoviedb.org/3/movie/{movie}/{api}?api_key={api_key}&language=en-US'

        
        title_url =endpoint.format(movie=movie_id,api="alternative_titles",api_key=MovieDB_KEY)
        title_result={}
        credit_url=endpoint.format(movie=movie_id,api="credits",api_key=MovieDB_KEY)
        credit_result={}
        image_url=endpoint.format(movie=movie_id,api="images",api_key=MovieDB_KEY)
        image_result={}
        keyword_url=endpoint.format(movie=movie_id,api="keywords",api_key=MovieDB_KEY)
        keyword_result={}
        release_url=endpoint.format(movie=movie_id,api="release_dates",api_key=MovieDB_KEY)
        release_result={}
        videos_url=endpoint.format(movie=movie_id,api="videos",api_key=MovieDB_KEY)
        videos_result={}
        reviews_url=endpoint.format(movie=movie_id,api="reviews",api_key=MovieDB_KEY)
        reviews_result={}

        #FOR ALTERNATIVE TITLE
        title_response = requests.get(title_url)
        if title_response.status_code == 200:  # SUCCESS
            title_result = title_response.json()
            title_result['success'] = True
            title_result['title']=title
            
        else:
            title_result['success'] = False
            if title_response.status_code == 404:  # NOT FOUND
                title_result['message'] = 'No entry found for "%s"' % movie_id
            else:
                title_result['message'] = 'Not available at the moment. Please try again later.'
        
        #FOR Credits
        credit_response = requests.get(credit_url)
        if credit_response.status_code == 200:  # SUCCESS
            credit_result = credit_response.json()
            credit_result['success'] = True
            
            
        else:
            credit_result['success'] = False
            if credit_response.status_code == 404:  # NOT FOUND
                credit_result['message'] = 'No entry found for "%s"' % movie_id
            else:
                credit_result['message'] = 'Not available at the moment. Please try again later.'
        

       

        #FOR Images
        image_response = requests.get(image_url)
        if image_response.status_code == 200:  # SUCCESS
            image_result = image_response.json()
            image_result['success'] = True
            
            
        else:
            image_result['success'] = False
            if image_response.status_code == 404:  # NOT FOUND
                image_result['message'] = 'No entry found for "%s"' % movie_id
            else:
                image_result['message'] = 'Not available at the moment. Please try again later.'
        

        

        #FOR Keywords
        keyword_response = requests.get(keyword_url)
        if keyword_response.status_code == 200:  # SUCCESS
            keyword_result = keyword_response.json()
            keyword_result['success'] = True
            
            
        else:
            keyword_result['success'] = False
            if keyword_response.status_code == 404:  # NOT FOUND
                keyword_result['message'] = 'No entry found for "%s"' % movie_id
            else:
                keyword_result['message'] = 'Not available at the moment. Please try again later.'
        

       

        #FOR Release information
        release_response = requests.get(release_url)
        if release_response.status_code == 200:  # SUCCESS
            release_result = release_response.json()
            release_result['success'] = True
            
            
        else:
            release_result['success'] = False
            if release_response.status_code == 404:  # NOT FOUND
                release_result['message'] = 'No entry found for "%s"' % movie_id
            else:
                release_result['message'] = 'Not available at the moment. Please try again later.'
        

        
        #FOR Videos
        videos_response = requests.get(videos_url)
        if videos_response.status_code == 200:  # SUCCESS
            videos_result = videos_response.json()
            videos_result['success'] = True
            
            
        else:
            videos_result['success'] = False
            if videos_response.status_code == 404:  # NOT FOUND
                videos_result['message'] = 'No entry found for "%s"' % movie_id
            else:
                videos_result['message'] = 'Not available at the moment. Please try again later.'
        

        

        #FOR Reviews
        reviews_response = requests.get(reviews_url)
        if reviews_response.status_code == 200:  # SUCCESS
            reviews_result = reviews_response.json()
            reviews_result['success'] = True
            
            
        else:
            reviews_result['success'] = False
            if reviews_response.status_code == 404:  # NOT FOUND
                reviews_result['message'] = 'No entry found for "%s"' % movie_id
            else:
                reviews_result['message'] = 'Not available at the moment. Please try again later.'
        
        #combined Result
        result['atlernative_title']=title_result
        result['credit']=credit_result
        result['image']=image_result
        result['keywords']=keyword_result
        result['release']=release_result
        result['video']=videos_result
        result['reviews']=reviews_result
        
        return render(request, 'movieSearch/movieDetail.html', { 'allAPI': result})



    