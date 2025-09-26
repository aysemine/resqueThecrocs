# 🐊 [Crocodile Conservation & Prediction Web App](https://resquethecrocs.streamlit.app/)

Spotted a crocodile and curious whether it’s endangered or not? This ML-powered guesser will come in handy!

This web application predicts crocodile conservation status using machine learning algorithms.  
It combines a **FastAPI backend**, a **Streamlit frontend**, and the **trained ML model**. 

You can check out the backend API [here](https://resquethecrocs.onrender.com/), powered by Render.


![Crocodile App Demo](gif.gif)

## Data Source

The dataset used for this project was obtained from Kaggle [Global Crocodile Species Dataset](https://www.kaggle.com/datasets/zadafiyabhrami/global-crocodile-species-dataset) by Bhrami Zadafiya, and contains features like length, weight, scientific name, genus, age class, sex, and habitat of crocodiles.




## Features

- Determine the conservation status of a crocodile based on its observed characteristics:
  - Length (m), Weight (kg)
  - Scientific Name, Genus
  - Age Class, Sex, Habitat
- Real-time predictions via API

## Project Structure

crocodile-app/  
├── backend/  
│   └── app.py  
├── ml/  
│   ├── rf_model_pca.pkl  
│   └── model_columns.json  
├── frontend/  
│   └── streamlit.py  
├── requirements.txt  
└── README.md  

