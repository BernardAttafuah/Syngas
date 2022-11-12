#imports important libraries
import streamlit as st
import sympy as smp
from sympy import*
st.set_page_config(
          page_title="Home Page",
          page_icon="🧊",
          layout="wide",
          initial_sidebar_state="expanded",
          )
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.write('Syngas Balanced Equation')
st.latex('''
CH_4 + H_2O  -> CO + 3H_2
''')
st.write('Where: A is CH4 & B  is H2O')
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
