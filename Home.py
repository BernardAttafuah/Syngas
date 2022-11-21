import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st
import sympy as smp
from sympy import*
import pandas as pd
import numpy as np



st.set_page_config(

    page_title='Syngas Operating Condition Analysis'
    
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


def streamlit_menu():
    if streamlit_menu:
        with st.sidebar:
            selected = option_menu(
                menu_title="App Menu",  
                options=["Home", "Equations - Used","Temperature & Conversion Graph Analysis",'Mole Flow & Conversion Graph Analysis','Temperature and Mole Flow Graph Analysis','About'],  
                icons=["house", "book", 'activity','graph-up-arrow','graph-down-arrow',"envelope"],  
                menu_icon="cast", 
                default_index=0
            )
        return selected
    
selected = streamlit_menu()
if selected == 'Home':
    
    def streamlit_menu_main():
        selectit = option_menu(
        menu_title="",  
        options=["Objective", "Default Values", "Animation",'PFD','P&ID'],  
        icons=['house-door', 'file lock2', "camera-reels-fill", 'pip-fill','pip'],  
        menu_icon="cast", 
        default_index=0,
        orientation='horizontal'
    )
        return selectit
   
    

    selectit = streamlit_menu_main()
    
    if selectit == "Objective":
    #setting up the variables
         st.info('''This user-friendly app is aimed at analysing the effects of operating parameters such as Methane and Steam flowrates, Temperature, Pressure etc of a **Syngas Process.**''' 
        
)
         st.info('The Analysis can be split into a **Temperature Profile** and a **Conversion Profile**')
         
         st.info('This work was inspired by the following personalities;')
         
         st.markdown('**Caleb Selase Sam**')
         st.markdown('**Prosper Jonas Ako**')
         st.markdown('**Danyl Oppong**')
         st.markdown('**Theophilus Baidoo**')
         st.markdown('**Godfrey Effah**')

         
    if selectit == "Default Values":
        
        df = pd.read_csv('default.csv'

        )
        st.table(df)
        data = {'Methane Flow Rate (mol/sec)':800,
            'Steam Flow Rate (mol/sec)':1600,
            'Initial Temperature (K)':2000,
            'Initial Pressure (bar)':30,
            #'Lower Integral Limit (kg)':min,
            'Upper Integral Limit (kg)':0.01
            }
        features = pd.DataFrame(data,index=[0])

#st.dataframe(features)
        st.table(data=features)
        st.latex(r'''
-       \Delta H_{rxn}^o = 205900 \frac{J}{mol}
        ''')
        st.info('The default values can be tweaked for better performance eg. Higher Conversion using **Graph Analysis** Tab from the **Navbar**' )

         
    if selectit == "Animation":
        st.write('Not available yet')

    
    if selectit == 'PFD':
        st.image('PFD.png')
    
    if selectit == 'P&ID':
        st.image('P&ID.png')


#displaying the dataframe in a static manner


if selected == "Equations - Used":

    #imports important libraries
    import streamlit as st
    import sympy as smp
    from sympy import*



    ########################################################

    #setting up the variables
    st.write('Mole Balance for Packed Bed Reactore - PBR')

    x,dF,dW,rate,FAo,dX,k,CA,CB,T,CAo = symbols('x dF dW rate FAo dX k CA CB T CAo',real = True,positive = True)
    epsilon,X,rate,FBo,W,r,DW,D_W,w,FA_O = symbols('epsilon X rate FBo W r DW D_W w FA_O',real = True,positive = True)

    st.latex(r'''
    -r_A = F_{Ao}\frac{dX_A}{dW}
    ''')
    st.write('Rate Equation - Elementary Reaction')
    st.write('Limiting Reactant: CH4')

    st.latex(r'''
    -r_A = kC_{CH4}C_{H2O}
    ''')
    st.latex(r'''
    k = 3\cdot 10^3\cdot e^{\frac{-15107}{T}}
    ''')

    st.write(r'''
    Where: k varies with Temperature
    ''')

    st.write('Phase: Gas Phase, variable density')

    st.latex(r'''
    v = vo(1 + \epsilon X_A) 
    ''')


    st.write('Assumptions: Non-Isothermal and Isobaric Process')

    st.latex(r'''
    C_A = \frac{C_{Ao}(1-X_A)}{1+ \epsilon X_A} \cdot\frac{T_o}{T}
    ''')

    st.write('Energy Balance: Steady State')

    st.latex(r'''
    Q - W - F_{Ao} \sum({\theta_i}C_Pi(T-T_o)) - F_{Ao}X[\Delta{H_{RX}^\degree}(T_R)+\Delta{C_p}(T-T_R)] =0
    ''')

    st.write('Assumptions: Adiabatic and No Shaft Work')
if selected == "Temperature & Conversion Graph Analysis":
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
   





    #######################################################

    st.markdown(

    '<div style = "text-align:center;"><b><h5>Summary of Selected Parameters<h/5></b></div>',unsafe_allow_html=True

    )
    st.sidebar.success('Input Operating Conditions')

    FAo = st.sidebar.number_input('Methane Flow Rate (mol/sec)',800,1000000)

    FBo = st.sidebar.number_input('Steam Flow Rate (mol/sec)',1600,1000000)
    To = st.sidebar.number_input('Initial Temperature (K)',1000,90000,2000)
    Po = st.sidebar.number_input('Initial Pressure (bar)',10,100,30)
    min = st.sidebar.number_input('Lower Integral Limit (kg)',0,0,0)
    max = st.sidebar.number_input('Upper Integral Limit (kg)',0.01,0.1,0.1)
    data = {'Methane Flow Rate (mol/sec)':FAo,
                'Steam Flow Rate (mol/sec)':FBo,
                'Initial Temperature (K)':To,
                'Initial Pressure (bar)':Po,
                #'Lower Integral Limit (kg)':min,
                #'Upper Integral Limit (kg)':max
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
if selected == "Mole Flow & Conversion Graph Analysis":
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
                #'Upper Integral Limit (kg)':max
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
    #plt.plot(weight,od[:,0],c= 'r', linewidth=2.3)
    #plt.title('Temperature Profile')
    #plt.xlabel('Weight(Catalyst)-kg')
    #plt.ylabel('Temperature (K)')
    #plt.grid(c='g')
    #plt.show()
    #st.pyplot(fig1)'''
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
    


#########################################################
if selected == "Temperature and Mole Flow Graph Analysis":
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
                #'Upper Integral Limit (kg)':max
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
    #fig2 = plt.figure()
    #plt.plot(weight,od[:,1],c= 'b', linewidth=1.6)
    #plt.title('Conversion Profile')
    #plt.xlabel('Weight(Catalyst)-kg')
    #plt.ylabel('Conversion %')
    #plt.grid(c= 'g')
    #plt.show()
    #st.pyplot(fig2)
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
    








#########################################################






####################################################
if selected == "About":
    import streamlit as st
    from contact_function import st_button, load_css
    from PIL import Image


    load_css()


    col1, col2, col3 = st.columns(3)
    col2.image(Image.open('pic.png'))

    st.header('Bernard Attafuah')

    st.info('Aspiring Chemical Process Engineer, AI and ML Enthusiast  with an interest in Plant Design')

    icon_size = 26
    st_button('linkedin', 'https://www.linkedin.com/in/bernardattafuah/', 'Follow me on LinkedIn', icon_size)
    st_button('github', 'https://github.com/BernardAttafuah/Gasification', 'Github Page', icon_size)
    st_button('email', 'https://sendfox.com/dataprofessor/', 'bernardattafuah@gmail.com', icon_size)
