import streamlit as st
import pandas as pd
from sympy import *
import sympy as smp
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import sklearn as skl
import matplotlib.pyplot as plt
import graphAnalysis #self made function
import countColumns #self made function
import seaborn as sns
import warnings
import xgboost
import IPython as ipy
import joblib
import pycaret
import numpy as np
from scipy import *
from scipy.integrate import *
import math
import IPython as ipy
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
import numpy as np
st.write('''
# Simple **Gasification** Prediction Performance

This app predicts the heating value of Syngas using fatures such as

1.Fixed Carbon (FC) 
2.Volatile Matter (VC)
3.ASH (MM)
4.Air Feeding (Nm^3/Kg)
5.Steam Feeding (kg/kg)
''')

st.sidebar.header('User Input Parameters')

def user_input():
    Fixed_Carbon_FC= st.sidebar.slider('Fixed Carbon (FC)',0,100,60)
    Volatile_Matter_VC= st.sidebar.slider('Volatile Matter (VC)',0,100,20)
    ASH = st.sidebar.slider('ASH (MM)',0,100,20)
    Air_Feeding = st.sidebar.slider('Air Feeding (Nm^3/Kg)',1.1,3.8,1.5)
    Steam_Feeding= st.sidebar.slider('Steam Feeding (kg/kg)',0.1,0.9,0.2)
    Tempeature_C =st.sidebar.slider('Temperature (C)',800,1500,900)
    sum = Fixed_Carbon_FC+Volatile_Matter_VC+ASH
    #if sum !=100:
        #print('Summation must be 100')
    #else:
    data = {'Fixed Carbon (FC)':Fixed_Carbon_FC,
                'Volatile Matter (VC)':Volatile_Matter_VC,
                'ASH (MM)':ASH,
                'Air Feeding (Nm^3/Kg)':Air_Feeding,
                'Steam Feeding (kg/kg)':Steam_Feeding,
                'Temperature (C)':Tempeature_C}
    features = pd.DataFrame(data,index=[0])
    return features

data_f = user_input()
    
st.subheader('User input parameters')
st.write(data_f)
df = pd.read_csv('dataset.csv')



from pycaret.regression import *
exp = setup(data=df,target='Heat Value (MJ/m^3)', normalize=False,remove_outliers=True,silent=True)
#Extracting parameters from pycaret's experiment
X = get_config(variable='X')
#X.head()
X_test = get_config(variable='X_test')
X_train = get_config(variable='X_train')
y_train= get_config(variable='y_train')
y_trained= get_config(variable='y_train')
y_test= get_config(variable='y_test')
#X_test.head()
y_test = pd.DataFrame(y_test).reset_index(drop=True)
y_trained = pd.DataFrame(y_trained).reset_index(drop=True)
#y_test 

model = load_model('savedmodel')

pred = predict_model(model,data=data_f)
pred['Predicted Heating Value MJ/m^3'] = pred['Label']
value = pred['Predicted Heating Value MJ/m^3']
st.write(round((value),1))
evaluate_model(model)
x,dF,dW,rate,FAo,dX,k,CA,CB,T,CAo = symbols('x dF dW rate FAo dX k CA CB T CAo',real = True,positive = True)
epsilon,X,rate,FBo,W,r,DW,D_W,w,FA_O = symbols('epsilon X rate FBo W r DW D_W w FA_O',real = True,positive = True)

#########################################
##### Introducing integral on both sides
FAo = 1000
FBo = 1500
phi = FBo/FAo
yAo = FAo/(FAo+FBo)
epsilon = ((4-2)*yAo)
Po = 30*(10**5) # Pascal
R = 8.314
To =1000 #Kelvin
CAo = round(((Po/(R*To)) * yAo),4)
T = 1237 #Kelvin
k = round(3 * 10 **5 * smp.exp(-15107/T),4)
CA = (CAo *(1-X))/(1+epsilon*X)
CB = (CAo *(phi-X))/(1+epsilon*X)
rate = k * CA * CB
