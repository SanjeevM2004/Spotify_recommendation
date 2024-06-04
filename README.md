# Spotify_recommendation
This Streamlit application recommends songs based on a user's input. It uses a pre-trained model to find similar songs from a dataset of Spotify tracks.

## Requirements
```
Python 3.6 or later
Streamlit
pickle
requests
fuzzywuzzy
```
## Installation

Make sure you have Python 3.6 or later installed. You can check this by running python --version in your terminal.
Install the required libraries using pip:
```bash
pip install -r requirements.txt
```

## Data Files

The application relies on two pre-built pickle files:

song_list.pkl: This file contains information about the Spotify tracks, including track name and ID.
song_similarity.pkl: This file contains a similarity matrix that represents how similar each song is to other songs in the dataset.
Instructions

Download the song_list.pkl and song_similarity.pkl files. You can place them in the same directory as your Python script.
Run the script using streamlit run app.py (where app.py is the name of your Python file).
Usage

The application has a text box where you can enter the name of a song. You can also use the slider to specify the number of recommendations you want. Clicking the "Recommend" button will generate a list of similar songs along with links to open them in Spotify.

## Code Structure

The code is divided into several sections:

`Downloading data files`: This section checks if the required pickle files exist and downloads them from a GitHub repository if they are not found.
`Loading models`: This section loads the song_list.pkl and song_similarity.pkl files into Python objects.
`Recommend function`: This function takes the name of a song and the number of recommendations as input. It uses fuzzy matching to find the closest song in the dataset and then retrieves similar songs based on the similarity matrix.
`Streamlit UI`: This section creates the Streamlit user interface, including the title, text box, slider, and recommendation list.

## Usage

```bash
streamlit run app.py
```

## Customization

You can customize the appearance of the application by editing the CSS code in the Streamlit markdown sections.
The code currently downloads the data files from a GitHub repository. You can modify the URLs to point to a different location if needed.
I hope this readme file is helpful!
