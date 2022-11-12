import numpy as np
import pandas
from scipy import *
from scipy.integrate import *
import math
import IPython as ipy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
st.set_page_config(
    page_title='PBR Operating Condition Analysis'   
)
st.markdown(

'<div style = "text-align:center;"><b><h5>Summary of Selected Parameters<h/5></b></div>',unsafe_allow_html=True

)
st.sidebar.success('Input Operating Conditions')

FAo = st.sidebar.number_input('Methane Flow Rate (mol/sec)',500,1000000)

FBo = st.sidebar.number_input('Steam Flow Rate (mol/sec)',500,1000000)
To = st.sidebar.number_input('Initial Temperature (K)',1000,90000,1000)
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

def model(X,w):
    x = X[0]
    y = X[1]
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
    dzdt = [dxdt,dydt]
    return dzdt

###############################################

zo = [To, 0]
w = np.linspace(min,max)
o = odeint(model,zo,w)
fig1 = plt.figure()
plt.plot(w,o[:,0],c= 'r', linewidth=2.3)
plt.title('Temperature Profile')
plt.xlabel('Weight(Catalyst)-kg')
plt.ylabel('Temperature (K)')
plt.grid(c='g')
plt.show()
st.pyplot(fig1)
fig2 = plt.figure()
plt.plot(w,o[:,1],c= 'b', linewidth=2.3)
plt.title('Conversion Profile')
plt.xlabel('Weight(Catalyst)-kg')
plt.ylabel('Conversion %')
plt.grid(c= 'g')
plt.show()
st.pyplot(fig2)


###############################################
def model(x,y,w):
    T_Reference = 298
    R=8.314
    yAo=FAo/(FBo+FAo)
    CAo= (yAo*(Po*(10**5)))/(R*To)
    CBo =  ((1-yAo)*(Po*(10**5)))/(R*To)
    delta_Cp= (3*CpH2)+CpCO-CpH2O-CpCH4
    Phi_B=FBo/FAo
    epsilon = yAo*((3+1)-(1+1))
    CA=(CAo*(1-y)*To)/(x*(1+(epsilon*y)))
    CC=(CAo*(y)*To)/(x*(1+(epsilon*y)))
    CD=(CAo*(3*y)*To)/(x*(1+(epsilon*y)))
    CB=(CAo*(Phi_B-y)*To)/(x*(1+(epsilon*y)))
    k=(3*(10**5))*math.exp((-15107/x))
    Rate=k*CA*CB
    H_rxn_T=standard_enthalpy_reaction+ delta_Cp*(x-T_Reference)
    dxdt = ((-H_rxn_T*Rate)/(FAo*(delta_Cp*y+(CpCH4+Phi_B*CpH2O))))
    dydt = (Rate/FAo)
    dzdt = [CA,CB,CC,CD,CAo,CBo]
    return dzdt
######################################################
#CA,CB,CC,CD,CAo,CBo = model(x=1700,y=0.6,w=0.02)
#st.write('The Initial concentration of A is: '+ str(round(CAo,3))+' mol/m^3')
#st.write('The Initial concentration of B is: '+ str(round(CBo,3))+' mol/m^3')
#st.write('The Final concentration of A is: '+ str(round(CA,3))+' mol/m^3')
#st.write('The Final concentration of B is: '+ str(round(CB,3))+' mol/m^3')
#st.write('The Final concentration of C is: '+ str(round(CC,3))+' mol/m^3')
#st.write('The Final concentration of D is: '+ str(round(CD,3))+' mol/m^3')
#####################################################



#####################################################



####################################################
