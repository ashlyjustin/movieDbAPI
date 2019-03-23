from django import forms
from django.conf import settings
import requests
import os
from decouple import config

class DictionaryForm(forms.Form):
    movie = forms.CharField(max_length=100)

    def search(self):
        result = {}
        movie = self.cleaned_data['movie']
        MovieDB_KEY = config('MovieDB_APP_Key')
        # key= os.environ.get('MovieDB_APP_Key')
        endpoint = 'https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=en-US&query={movie_id}'

        
        url2 =endpoint.format(api_key=MovieDB_KEY, movie_id=movie)
        

        print(url2)
        response = requests.get(url2)
        if response.status_code == 200:  # SUCCESS
            result = response.json()
            result['success'] = True
        else:
            result['success'] = False
            if response.status_code == 404:  # NOT FOUND
                result['message'] = 'No entry found for "%s"' % movie
            else:
                result['message'] = 'Not available at the moment. Please try again later.'
        return result