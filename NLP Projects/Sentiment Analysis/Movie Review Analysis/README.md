# Movie Review Sentiment Analysis

## Overview
This project focuses on analyzing movie reviews to predict sentiments using various machine learning techniques. Utilizing a dataset of 50,000 IMDB movie reviews, the project applies natural language processing (NLP) to clean and preprocess the data, including removing HTML tags, URLs, non-alphanumeric characters, and stop words. It also employs stemming to reduce words to their root form. The analysis includes exploratory data analysis (EDA) to understand the distribution of sentiments and the most common words in positive and negative reviews.

## Features
- **Data Cleaning and Preprocessing**: Lowercasing, removing special characters, URLs, and stop words, tokenization, and stemming.
- **Exploratory Data Analysis (EDA)**: Sentiment distribution, word counts, and visualization of the most frequent words using word clouds and bar plots.
- **Machine Learning Models**: Logistic Regression, Multinomial Naive Bayes, and Linear Support Vector Machine (SVM) models are trained and evaluated. Model performance is optimized using grid search.

## Requirements
- Python 3.8+
- Libraries: Pandas, Matplotlib, Seaborn, Plotly, NLTK, scikit-learn, WordCloud, and more.

## Dataset
The dataset consists of 50,000 IMDB movie reviews, labeled with sentiments (positive or negative).

## Usage
1. Install required libraries: `pip install -r requirements.txt`
2. Run the Jupyter notebook to preprocess data, perform EDA, and train models.
3. Evaluate model performance and select the best model for deployment.

## Conclusion
The project demonstrates the effectiveness of NLP and machine learning techniques in sentiment analysis of movie reviews, with Logistic Regression, Multinomial Naive Bayes, and Linear SVM showing promising results.

## Authors
- Avashesh Kumar

