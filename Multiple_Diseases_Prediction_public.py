# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 19:55:45 2022

@author: santosh
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

breast_cancer_data_model = pickle.load(open('breast_cancer_data_model.sav', 'rb'))

#diabetes_model = pickle.load(open('C:/Users/santo/OneDrive/Desktop/Multiple Diseases Prediction using Machine Learning/diabetes_model.sav','rb'))
#heart_disease_model = pickle.load(open('C:/Users/santo/OneDrive/Desktop/Multiple Diseases Prediction using Machine Learning/heart_disease_model.sav','rb'))
#parkinsons_model = pickle.load(open('C:/Users/santo/OneDrive/Desktop/Multiple Diseases Prediction using Machine Learning/parkinsons_model.sav','rb'))
#breast_cancer_data_model = pickle.load(open('C:/Users/santo/OneDrive/Desktop/Multiple Diseases Prediction using Machine Learning/breast_cancer_data_model.sav', 'rb'))

# sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Attack Prediction',
                           'Parkinsons Prediction',
                           'Breast Cancer Prediciton'],
                          icons=['droplet','activity','eyedropper','gender-female'],
                          default_index=0)
    
    # Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies (Ex: 0,17)')
        
    with col2:
        Glucose = st.text_input('Glucose Level (Ex: 0,163)')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value (Ex: 0,122)')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value (Ex: 0,99)')
    
    with col2:
        Insulin = st.text_input('Insulin Level (Ex: 0,846)')
    
    with col3:
        BMI = st.text_input('BMI value (Ex: 0,67.1)')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value (Ex: 0.078,2.42)')
    
    with col2:
        Age = st.text_input('Age of the Person (Ex: 21,81)')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, 
                                                   SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Attack Prediction'):
    
    # page title
    st.title('Heart Attack Prediction')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age (Ex: 29,77)')
        
    with col2:
        sex = st.number_input('Sex (Ex: 0,1)')
        
    with col3:
        cp = st.number_input('Chest Pain types (Ex: 0,3)')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure (Ex: 94,200)')
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl (Ex: 126,564)')
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (Ex: 0,1)')
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results (Ex: 0,2)')
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved (Ex: 71,202)')
        
    with col3:
        exang = st.number_input('Exercise Induced Angina (Ex: 0,1)')
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise (Ex: 0,6.2)')
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment (Ex: 0,2)')
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy (Ex: 0,4)')
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect (Ex: 0,3)')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol,
                                                         fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'This person most likely to have Heart Attack'
        else:
          heart_diagnosis = 'Theis person less likely to have Heart Attack'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction")
    
    col1, col2, col3, col4 = st.columns(4)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz) (Ex:88.33,260.105)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz) (Ex: 102.145,592.03)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz) (Ex: 65.476,239.17)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%) (Ex: 0.00168,0.03316)')
        
    with col1:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs) (Ex: 0.000007,0.00026)')
        
    with col2:
        RAP = st.text_input('MDVP:RAP (Ex: 0.00068,0.02144)')
        
    with col3:
        PPQ = st.text_input('MDVP:PPQ (Ex: 0.00092,0.01958)')
        
    with col4:
        DDP = st.text_input('Jitter:DDP (Ex: 0.00204,0.06433)')
        
    with col1:
        Shimmer = st.text_input('MDVP:Shimmer (Ex: 0.00954,0.11908)')
        
    with col2:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB) (Ex: 0.085,1.302)')
        
    with col3:
        APQ3 = st.text_input('Shimmer:APQ3 (Ex: 0.00455,0.05647)')
        
    with col4:
        APQ5 = st.text_input('Shimmer:APQ5 (Ex: 0.0057,0.0794)')
        
    with col1:
        APQ = st.text_input('MDVP:APQ (Ex: 0.00719,0.13778)')
        
    with col2:
        DDA = st.text_input('Shimmer:DDA (Ex: 0.01364,0.16942)')
        
    with col3:
        NHR = st.text_input('NHR (Ex: 0.00065,0.31482)')
        
    with col4:
        HNR = st.text_input('HNR (Ex: 8.441,33.047)')
        
    with col1:
        RPDE = st.text_input('RPDE (Ex: 0.25657,0.685151)')
        
    with col2:
        DFA = st.text_input('DFA (Ex: 0.574282,0.825288)')
        
    with col3:
        spread1 = st.text_input('spread1 (Ex: -7.964984,-2.434031)')
        
    with col4:
        spread2 = st.text_input('spread2 (Ex: 0.006274,0.450493)')
        
    with col1:
        D2 = st.text_input('D2 (Ex: 1.423287,3.671155)')
        
    with col2:
        PPE = st.text_input('PPE (Ex: 0.044539,0.527367)')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent,
                                                           Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,
                                                           APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,
                                                           DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person will have Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person will not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
    
    

# Breast Cancer Prediction Page
if (selected == "Breast Cancer Prediciton"):
    
    # page title
    st.title("Breast Cancer Prediciton")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        radius_mean = st.text_input('Radius of Lobes (Ex:6.98,28.1)')
        
    with col2:
        texture_mean = st.text_input('Mean of Surface Texture (Ex: 9.71,39.3)')
        
    with col3:
        perimeter_mean = st.text_input('Outer Perimeter of Lobes (Ex: 43.8,189)')
        
    with col4:
        area_mean = st.text_input('Mean Area of Lobes (Ex: 144,2500)')
        
    with col5:
        smoothness_mean = st.text_input('Mean of Smoothness Levels (Ex: 0.05,0.16)')
        
    with col1:
        compactness_mean = st.text_input('Mean of Compactness (Ex: 0.02,0.35)')
        
    with col2:
        concavity_mean = st.text_input('Mean of Concavity (Ex: 0,0.43)')
        
    with col3:
        concave_points_mean = st.text_input('Mean of Cocave Points (Ex: 0,0.2)')
        
    with col4:
        symmetry_mean = st.text_input('Mean of Symmetry (Ex: 0.11,0.3)')
        
    with col5:
        fractal_dimension_mean = st.text_input('Mean of Fractal Dimension (Ex: 0.05,0.1)')
        
    with col1:
        radius_se = st.text_input('SE of Radius (Ex: 0.11,2.87)')
        
    with col2:
        texture_se = st.text_input('SE of Texture (Ex: 0.36,4.88)')
        
    with col3:
        perimeter_se = st.text_input('Perimeter of SE (Ex: 0.76,22)')
        
    with col4:
        area_se = st.text_input('Area of SE (Ex: 6.8,542)')
        
    with col5:
        smoothness_se = st.text_input('SE of Smoothness (Ex: 0,0.03)')
        
    with col1:
        compactness_se = st.text_input('SE of compactness (Ex: 0,0.14)')
        
    with col2:
        concavity_se = st.text_input('SEE of concavity (Ex: 0,0.4)')
        
    with col3:
        concave_points_se = st.text_input('SE of concave points (Ex: 0,0.05)')
        
    with col4:
        symmetry_se = st.text_input('SE of symmetry (Ex: 0.01,0.08)')
        
    with col5:
        fractal_dimension_se = st.text_input('SE of Fractal Dimension (Ex: 0,0.03)')
        
    with col1:
        radius_worst = st.text_input('Worst Radius (Ex: 7.93,36)')
        
    with col2:
        texture_worst = st.text_input('Worst Texture (Ex: 12,49.5)')
    
    with col3:
        perimeter_worst = st.text_input('Worst Perimeter (Ex: 50.4,251)')
        
    with col4:
        area_worst = st.text_input('Worst Area (Ex: 185,4250)')
            
    with col5:
        smoothness_worst = st.text_input('Worst Smoothness (Ex: 0.07,0.22)')
                
    with col1:
        compactness_worst = st.text_input('Worse Compactness (Ex: 0.03,1.06)')
                    
    with col2:
        concavity_worst = st.text_input('Worst Concavity (Ex: 0,1.25)')
                        
    with col3:
        concave_points_worst = st.text_input('Worst Concave Points (Ex: 0,0.29)')
                            
    with col4:
        symmetry_worst = st.text_input('Worst Symmetry (Ex: 0.16,0.66)')
                                
    with col5:
        fractal_dimension_worst = st.text_input('Worst Fractal Dimension (Ex: 0.06,0.21)')
        
    
    
    # code for Prediction
    Breast_cancer_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Breast Cancer Test Result"):
        Breast_cancer_prediction = breast_cancer_data_model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean,
                                                           smoothness_mean, compactness_mean, concavity_mean,concave_points_mean,
                                                           symmetry_mean,fractal_dimension_mean,
                                                           radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,
                                                           concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,
                                                           radius_worst,texture_worst,perimeter_worst,area_worst,
                                                           smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,
                                                           symmetry_worst,fractal_dimension_worst]])                          
        
        if (Breast_cancer_prediction[0] == 1):
          Breast_cancer_diagnosis = "This person have malignant (cancerous) breast."
        else:
          Breast_cancer_diagnosis = "This person does not have benign (non-cancerous) breast."
        
    st.success(Breast_cancer_diagnosis)
    


























