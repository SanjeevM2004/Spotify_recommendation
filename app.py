import streamlit as st
import pickle
import requests
from fuzzywuzzy import process
import os

repo_owner = 'SanjeevM2004'
repo_name = 'Spotify_recommendation'
release_tag = 'v1.0.0'
#https://github.com/SanjeevM2004/Spotify_recommendation/releases/download/v1.0.0/song_list.pkl
song_list_url = f'https://github.com/{repo_owner}/{repo_name}/releases/download/{release_tag}/song_list.pkl'
similarity_url = f'https://github.com/{repo_owner}/{repo_name}/releases/download/{release_tag}/song_similarity.pkl'

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

# Download files from GitHub release
if not os.path.exists('song_list.pkl'):
    download_file(song_list_url, 'song_list.pkl')
if not os.path.exists('song_similarity.pkl'):
    download_file(similarity_url, 'song_similarity.pkl')

# Load the models
song_list = pickle.load(open('song_list.pkl', 'rb'))
similarity = pickle.load(open('song_similarity.pkl', 'rb'))

def recommend(song,  number):
    # Use fuzzy matching to find the closest match
    closest_match = process.extractOne(song, song_list['Track Name'])[0]
    index = song_list[song_list['Track Name'] == closest_match].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_songs = []
    for i in distances[1:number+1]:
        track_id_detail = song_list.iloc[int(i[0])]['Track_id']
        track_name_detail = song_list.iloc[int(i[0])]['Track Name']
        recommended_songs.append((track_name_detail, track_id_detail))
    return recommended_songs

# Custom CSS for background and image styling
st.markdown(
    """
    <style>
    .green {
        color: rgb(29, 185, 84);
    }
    """,
    unsafe_allow_html=True
)
import streamlit as st

# Include custom CSS to style the button
st.markdown(
    """
    <style>
    .green-button {
        background-color: rgb(29, 185, 84);
        font: times new roman;
        color: black;
        border: black;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<style>
  .stApp{
    background-image: url("https://cdn.hashnode.com/res/hashnode/image/upload/v1618683315311/KuMns646J.png?w=1600&h=840&fit=crop&crop=entropy&auto=compress,format&format=webp");
    background-size: cover; /* Stretch image to fill the entire viewport */
    color: white;
  }
  
  .row {
    display: flex;
    font-weight: bold;
    font-size: 20px;
    flex-wrap: wrap; /* Ensure items wrap to next line */
    justify-content: space-around;
    margin: 0px 10px;
  }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="green">Spotify recommendation tool</h1>', unsafe_allow_html=True)

selected_song = st.text_input('Type a name of a song:', '')
number = st.slider("Number of songs", min_value=1, max_value=20, value=5)
if st.markdown('<button class="green-button">Recommend</button>', unsafe_allow_html=True):
  if selected_song:
    recommendations = recommend(selected_song, number)
    if recommendations:
        st.markdown("<div class='row'>", unsafe_allow_html=True)
        for i, (song_name, song_link) in enumerate(recommendations):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**{song_name}**")
            with col2:
                st.markdown(f"<a href='https://open.spotify.com/track/{song_link}' target='_blank' style='text-decoration:none;'><button class='green-button'>Open in Spotify</button></a>", unsafe_allow_html=True)
        # Close the row div after all recommendations are displayed
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.write("No recommendations found.")
  else:
    st.write("Please enter a song name.")
