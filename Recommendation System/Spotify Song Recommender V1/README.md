# Spotify Song Recommendation System

## Project Overview
This project develops a music recommendation system using the Spotify song dataset available on Kaggle. Leveraging machine learning and natural language processing techniques, the system suggests songs to users based on the similarity of the song mentioned to the other songs based on the lyrics.

## Features
- **Data Utilization**: Employs a comprehensive dataset from Spotify containing various song attributes.
- **Personalized Recommendations**: Generates song suggestions using similarity of lyrics.
- **Machine Learning Integration**: Utilizes a sophisticated machine learning model for accurate prediction and matching.

## Dataset
The Spotify song dataset includes numerous attributes for each track, such as genre, artist, tempo, and more, facilitating a detailed analysis and understanding of user preferences. The dataset can be found on [Kaggle](https://www.kaggle.com/).

## Implementation Details

### Data Preprocessing
The dataset undergoes thorough preprocessing to ensure optimal model performance.

### Model Training and Evaluation
A detailed process is undertaken to train and evaluate the machine learning model, ensuring high accuracy and user satisfaction with the recommendations provided. The model training process is documented in `modeltraining.pdf`.

### Application Interface
`app.py` serves as the entry point for the recommendation system, featuring a user-friendly interface for interaction and song discovery.

## Getting Started

### Prerequisites
- Python 3.x
- Pandas
- Scikit-learn
- Spotipy for Spotify API interaction
- Streamlit
- altair == 4.0

### Installation
Install the required packages using pip:
pip install pandas scikit-learn spotipy streamlit

### Running the Application
Execute the following command to start the recommendation system:
streamlit run app.py

## How It Works
Users input their favorite songs, and the system processes this information to recommend similar tracks from the Spotify dataset. The recommendations are based on analyzing song similarity in lyrics.
