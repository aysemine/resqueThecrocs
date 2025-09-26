# 🐊 [Crocodile Conservation & Prediction Web App](https://resquethecrocs.streamlit.app/)

Spotted a crocodile and curious whether it’s endangered or not? This ML-powered guesser will come in handy!

This web application predicts crocodile conservation status using machine learning algorithms.  
It combines a **FastAPI backend**, a **Streamlit frontend**, and the **trained ML model**.

![Crocodile App Demo](gif.gif)

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

