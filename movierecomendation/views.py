from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import load_movies_dict_model,load_similarity_model
import pandas as pd

similarity = load_similarity_model()
movies_dict = load_movies_dict_model()
movies= pd.DataFrame(movies_dict)
#print([movies['title'] == 'Avatar'].index[0])

class recomadationView(APIView):
    
    def get_recommend(self,movie):
        #movies= pd.DataFrame(movies_dict)
        movie_index =   movies[movies['title'] == movie].index[0]
        #print(movie_index,movie)
        try:
            
            distances = similarity[movie_index]
            moviesList = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

            recommend_movies = []

            for i in moviesList:
                recommend_movies.append(movies.iloc[i[0]].title)

            return recommend_movies
        except Exception as e:
                print(e)
                print(movie)
                return None
    
    def post(self,request):
        try:
            movie_name = request.data.get("movie_name")
            if not movie_name:
                return Response({'error':'No movie name provided'}, status=status.HTTP_400_BAD_REQUEST)
            recommend_movie = self.get_recommend(movie_name)
            if not recommend_movie:
                return Response({'error':'No recommend found'}, status=status.HTTP_404_NOT_FOUND)
            return Response({'recommend':recommend_movie}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
