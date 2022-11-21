import numpy as np
import pandas
from scipy import *
from scipy.integrate import *
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

#####################################################
st.set_page_config(

    page_title='PBR Operating Condition Analysis'
    
)


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
             p {
            text-align: center;
            }
            </style>
           
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


#######################################################

st.markdown(

'<div style = "text-align:center;"><b><h5>Summary of Selected Parameters<h/5></b></div>',unsafe_allow_html=True

)
st.sidebar.success('Input Operating Conditions')

FAo = st.sidebar.number_input('Methane Flow Rate (mol/sec)',800,1000000)

FBo = st.sidebar.number_input('Steam Flow Rate (mol/sec)',1600,1000000)
To = st.sidebar.number_input('Initial Temperature (K)',1000,90000,2000)
Po = st.sidebar.number_input('Initial Pressure (bar)',20,100,30)
min = st.sidebar.number_input('Lower Integral Limit (kg)',0,0,0)
max = st.sidebar.number_input('Upper Integral Limit (kg)',0.01,0.1,0.1)

data = {'Methane Flow Rate (mol/sec)':FAo,
            'Steam Flow Rate (mol/sec)':FBo,
            'Initial Temperature (K)':To,
            'Initial Pressure (bar)':Po,
            #'Lower Integral Limit (kg)':min,
            'Upper Integral Limit (kg)':max
            }
features = pd.DataFrame(data,index=[0])

#st.dataframe(features)
st.table(data=features)



#####################################################

#FAo= 1000# mol/sec
#FBo= 1500# mol/sec
#To=2800#Kelvin
#Po=30*(10**5)#Pascal
CpCO=32.455#J/mol/Kelvin
CpH2O=39.93#J/mol/Kelvin
CpH2=29.915#J/mol/Kelvin
CpCH4=67.184#J/mol/Kelvin
standard_enthalpy_reaction=205900 #J/mol
#min = 0#min starting integration value
#max = 0.01#max starting integrating value


def model2(X,w):
    x = X[0]
    y = X[1]
    Fao = X[2]
    Fbo = X[3]
    Fco = X[4]
    Fdo = X[5]
    T_Reference = 298
    R=8.314
    yAo=FAo/(FBo+FAo)
    CAo= (yAo*(Po*(10**5)))/(R*To)
    delta_Cp= (3*CpH2)+CpCO-CpH2O-CpCH4
    Phi_B=FBo/FAo
    epsilon = yAo*((3+1)-(1+1))
    CA=(CAo*(1-y)*To)/(x*(1+(epsilon*y)))
    CB=(CAo*(Phi_B-y)*To)/(x*(1+(epsilon*y)))
    k=(3*(10**5))*math.exp((-15107/x))
    Rate=k*CA*CB
    H_rxn_T=standard_enthalpy_reaction+ delta_Cp*(x-T_Reference)
    dxdt = ((-H_rxn_T*Rate)/(FAo*(delta_Cp*y+(CpCH4+Phi_B*CpH2O))))
    dydt = (Rate/FAo)
    dFA = (-k*CA*CB)
    dFB = (-k*CA*CB)
    dFC = (k*CA*CB)
    dFD = ((1/3)*k*CA*CB)
    dzdt = [dxdt,dydt,dFA,dFB,dFC,dFD]
    return dzdt

###############################################

z = [To, 0,FAo,FBo,0,0]
weight = np.linspace(min,max)
od = odeint(model2,z,weight)
fig1 = plt.figure()
plt.plot(weight,od[:,0],c= 'r', linewidth=2.3)
plt.title('Temperature Profile')
plt.xlabel('Weight(Catalyst)-kg')
plt.ylabel('Temperature (K)')
plt.grid(c='g')
plt.show()
st.pyplot(fig1)
fig2 = plt.figure()
plt.plot(weight,od[:,1],c= 'b', linewidth=1.6)
plt.title('Conversion Profile')
plt.xlabel('Weight(Catalyst)-kg')
plt.ylabel('Conversion %')
plt.grid(c= 'g')
plt.show()
st.pyplot(fig2)
fig3 = plt.figure()
plt.plot(weight,od[:,2],c= 'b', linewidth=1.6)
plt.plot(weight,od[:,3],c= 'g', linewidth=1.6)
plt.plot(weight,od[:,4],c= 'r', linewidth=1.6)
plt.plot(weight,od[:,5],c= 'y', linewidth=1.6)
plt.title('Mole Balance Profile')
plt.xlabel('Weight(Catalyst)-kg')
plt.ylabel('Mole Flow (mol/sec)')
plt.grid(c= 'k')
plt.legend(['CH4','Steam','CO','H2'])

plt.show()

st.pyplot(fig3)











#####################################################



####################################################
