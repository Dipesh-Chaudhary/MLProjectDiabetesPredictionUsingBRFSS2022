# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:39:58 2023

@author: Dell
"""
import numpy as np
import pickle 
import streamlit as st
import pandas as pd
import statistics
from sklearn.model_selection import train_test_split,cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

class KNN_Classifier1():

  # initiating the parameters
  def __init__(self,k,X,y):
        self.X_train = X
        self.y_train = y
        training_data=pd.concat([X_train,y_train], axis=1)
        self.training_data1= np.array(training_data)
        self.k=k



  # getting the  euclidean distance
  def get_distance(self,training_data_point, test_data_point):
      dist = 0
      dist = np.sum((training_data_point[:-1] - test_data_point)**2)

      euclidean_dist = np.sqrt(dist)

      return euclidean_dist



  # getting the nearest neighbors
  def nearest_neighbors(self, test_data):
    training_data1 = self.training_data1
    k=self.k
    distance_list = []
    for training_data_point in self.training_data1:
            distance = self.get_distance(training_data_point, test_data)
            distance_list.append((training_data_point, distance))

    distance_list.sort(key=lambda x: x[1])

    neighbors_list = [x[0] for x in distance_list[:k]]

    return neighbors_list


  # predict the class of the new data point:
  def predict(self, X_test):
        y_pred = []

        for test_data in X_test:
            neighbors = self.nearest_neighbors(test_data)
            label = [data[-1] for data in neighbors]
            predicted_class = statistics.mode(label)
            y_pred.append(predicted_class)

        return y_pred




loaded_model = pickle.load(open("C:/DIPESH/study materials/sixth sem/PROJECT FOLDER/original dataset/2022 SAS/6 Model Building/knnTrainedModelFromScratch.sav","rb"))

def diabetes_prediction(input_data):
    
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data,dtype=np.float64)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    
    
    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return'The person is diabetic'
     
        
def main():
    
    #TITLE
    st.title('Diabetes Prediction System')
    
    a=st.number_input('Enter BMI value',1,100,step=1)
    

    
    Box2=st.selectbox(
    'does the patient ever had stroke?',
    ('never had stroke / 0', 'had stroke / 1')
)
    if(Box2=='never had stroke / 0'):
        b=0
    else:
        b=1


    Box3=st.selectbox(
    'does the patient ever had heart attack?',
    ('never had heartattack / 0', 'had heartattack / 1')
)
    if(Box3=='never had heartattack / 0'):
        c=0
    else:
        c=1


    Box4=st.selectbox( 
    'When did the patient had last routine checkup?',
    ('Within past year / 1','Within past 2 years / 2','Within past 5 years / 3','5 or more years / 4')
)
    if(Box4=='Within past year / 1'):
        d=1
    elif(Box4=='Within past 2 years / 2'):
        d=2
    elif(Box4=='Within past 5 years / 3'):
        d=3
    else:
        d=4

    Box5=st.selectbox(
        'What\'s patient\'s general Health',
        ('Excellent / 1','Very Good / 2','Good / 3','Fair / 4','Poor / 5'))
    if(Box5=='Excellent / 1'):
        e=1
    elif(Box5=='Very Good / 2'):
        e=2
    elif(Box5=='Good / 3'):
        e=3
    elif(Box5=='Fair / 4'):
        e=4
    else:
        e=5

    f=st.number_input('for how many days during the past 30 days was your physical health not good? between 0-30',0, 30, step=1)


    Box7=st.selectbox(
    'Do patient have serious difficulty walking or climbing stairs?',
    ('no / 0', 'yes / 1')
)
    if(Box7=='no / 0'):
        g=0
    else:
        g=1


    Box8=st.selectbox(
        'What\'s the patient\'s age',
        ('18 to 24 / 1','25 to 29 / 2','30 to 34 / 3','35 to 39 / 4','40 to 44 / 5','45 to 49 / 6','50 to 54 / 7','55 to 59 / 8','60 to 64 / 9','65 to 69 / 10','70 to 74 / 11','75 to 79 / 12','80 or older / 13'))
    if(Box8=='18 to 24 / 1'):
        h=1
    elif(Box8=='25 to 29 / 2'):
        h=2
    elif(Box8=='30 to 34 / 3'):
        h=3
    elif(Box8=='35 to 39 / 4'):
        h=4
    elif(Box8=='40 to 44 / 5'):
        h=5
    elif(Box8=='45 to 49 / 6'):
        h=6
    elif(Box8=='50 to 54 / 7'):
        h=7
    elif(Box8=='55 to 59 / 8'):
        h=8
    elif(Box8=='60 to 64 / 9'):
        h=9
    elif(Box8=='65 to 69 / 10'):
        h=10
    elif(Box8=='70 to 74 / 11'):
        h=11
    elif(Box8=='75 to 79 / 12'):
        h=12
    else:
        h=13

    Box9=st.selectbox(
        'What\'s the patient\'s age',
        ('Less Than $10,000 / 1','$10,000 to $15,000 / 2','$15,000 to  $20,000 / 3','$20,000 to  $25,000 / 4','$25,000 to  $35,000 / 5','$35,000 to  $50,000 / 6','$50,000 to  $75,000 / 7','$75,000 to  $100,000 / 8','$100,000 to $150,000 / 9','$150,000 to  $200,000 / 10','$200,000 or more / 11'))
    if(Box9=='Less Than $10,000 / 1'):
        i=1
    elif(Box9=='$10,000 to $15,000 / 2'):
        i=2
    elif(Box9=='$15,000 to  $20,000 / 3'):
        i=3
    elif(Box9=='$20,000 to  $25,000 / 4'):
        i=4
    elif(Box9=='$25,000 to  $35,000 / 5'):
        i=5
    elif(Box9=='$35,000 to  $50,000 / 6'):
        i=6
    elif(Box9=='$50,000 to  $75,000 / 7'):
        i=7
    elif(Box9=='$75,000 to  $100,000 / 8'):
        i=8
    elif(Box9=='$100,000 to $150,000 / 9'):
        i=9
    elif(Box9=='$150,000 to  $200,000 / 10'):
        i=10
    else:
        i=11



    #for prediction
    
    diagnosis=''
    
    #buttons
    
    if st.button('Diabetes Test Result'):
        diagnosis= diabetes_prediction([a,b,c,d,e,f,g,h,i])
        
    st.success(diagnosis)


if __name__ == '__main__':
    main()