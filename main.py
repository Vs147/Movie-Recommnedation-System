import streamlit as st
import pandas as pd
import pickle
import requests
import gzip




def fetch_poster(movie_id):
     response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=714682f8fb4249cdc72fda2481c389d4".format(movie_id))
     data=response.json()
     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']



def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]
    recommended_movies=[]
    recommended_movies_images=[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_images.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_images

st.title("Movie Recommendation System")


movie_dict=pickle.load(open("movies_dict.pkl",'rb'))
movies=pd.DataFrame(movie_dict)

with gzip.open('test.pklz', 'rb') as ifp:
    print(pickle.load(ifp))
    similarity=pickle.load(ifp)

# similarity=pickle.load(open("similarity.pkl",'rb'),encoding='latin1')
# import pickle

# with open('Similarity.pkl', 'rb') as f:
#     similarity = pickle.load(f, encoding='latin1')



selected_movie = st.selectbox(
     'Select a movie:',
    movies['title'].values)



if st.button("Recommend"):
    names,posters=recommend(selected_movie)
    col1,col2,col3,col4,col5=st.columns(5)
    col7,col8,col9,col10,col11=st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

    with col7:
        st.text(names[5])
        st.image(posters[5])


    with col8:
        st.text(names[6])
        st.image(posters[6])

    with col9:
        st.text(names[7])
        st.image(posters[7])

    with col10:
        st.text(names[8])
        st.image(posters[8])

    with col11:
        st.text(names[9])
        st.image(posters[9])


