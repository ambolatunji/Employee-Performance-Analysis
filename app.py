import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
from sklearn.externals import joblib

#loading in the model to predict on the data

RF = open('INX_Future_IncRF.ml', 'rb')
RFclassifier = joblib.load(RF)

#XGB = open('INX_Future_IncXGB.ml', 'rb')
#XGBclassifier = joblib.load(XGB)

def main():
      # giving the webpage a title
    st.title("Employee Performance Prediction")
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
   # html_temp = '''<div style ="background-color:yellow;padding:13px">
   # <h1 style ="color:black;text-align:center;">Employee Performance Prediction</h1>
   # <br></br>
   # </div>'''
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    #st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
if __name__=='__main__':
    main()

def welcome():
	return 'welcome all'


if st.button('Show data'):
	data = pd.read_excel('INX_Future_Inc_Employee_Performance_CDS_Project2_Data_V1.8.xls')
	st.dataframe(data)


# defining the function which will make the prediction using 
# the data which the user inputs



def RFprediction(EmpDepartment, EmpJobRole, EmpEnvironmentSatisfaction, EmpLastSalaryHikePercent, EmpWorkLifeBalance, ExperienceYearsAtThisCompany, ExperienceYearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager):
	RFprediction = RFclassifier.predict([[EmpDepartment, EmpJobRole, EmpEnvironmentSatisfaction, EmpLastSalaryHikePercent, EmpWorkLifeBalance, ExperienceYearsAtThisCompany, ExperienceYearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager]])
	print(RFprediction)
	return RFprediction


#def XGBprediction(EmpDepartment, EmpJobRole, EmpEnvironmentSatisfaction, EmpLastSalaryHikePercent, EmpWorkLifeBalance, ExperienceYearsAtThisCompany, ExperienceYearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager):
 #   XGBprediction = RFclassifier.predict([[EmpDepartment, EmpJobRole, EmpEnvironmentSatisfaction, EmpLastSalaryHikePercent, EmpWorkLifeBalance, ExperienceYearsAtThisCompany, ExperienceYearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager]])
  #  print(XGBprediction)
   # return XGBprediction
# this is the main function in which we define our webpage 
    
    

#st.markdown("EmpEducationLevel:	1 'Below College' 2 'College' 3 'Bachelor' 4 'Master' 5 'Doctor'")
st.markdown('### 5:Sales, 0:Data-Science, 1:Develpment, 3:Human Resources, 2:Finance, 4:R & D')
EmpDepartment = st.selectbox('The Employee Department', [0, 1, 2, 3, 4, 5])#st.text_input("Employee Department", "Type Here")

EmpJobRole = st.slider("Employee Job Role", min_value=0, max_value=19, value=1, step=1, format='%f') #Check Datatframe #st.text_input("Employee JobRole", "Type Here")

EmpEnvironmentSatisfaction = st.slider("Environment Satisfaction", min_value=1, max_value=4, value=1, step=1, format='%f')#st.text_input("Environment Satisfaction", "Type Here")

EmpLastSalaryHikePercent = st.slider("Employee Salary Increment", min_value=0, max_value=5, value=1, step=1, format='%f')#st.text_input("Sepal Length", "Type Here")

#st.markdown("#### EmpWorkLifeBalance: 1 - Bad, 2 - Good, 3 - Better, 4 - Best")

EmpWorkLifeBalance = st.slider("Employee Work Life Balance", min_value=0, max_value=4, value=1, step=1, format='%f')#st.text_input("Sepal Length", "Type Here")

ExperienceYearsAtThisCompany = st.slider("Employee Experience Years", min_value=1, max_value=40, value=1, step=1, format='%f')#st.text_input("Sepal Length", "Type Here")

ExperienceYearsInCurrentRole = st.slider("Employee Experience Years In Current Role", min_value=0, max_value=18, value=1, step=1, format='%f')#st.text_input("Sepal Length", "Type Here")

YearsSinceLastPromotion = st.slider("Employee Last Promotion", min_value=0, max_value=15, value=1, step=1, format='%f')#st.text_input("Sepal Length", "Type Here")

YearsWithCurrManager = st.slider("Employee years spent with Current Manager", min_value=0, max_value=16, value=1, step=1, format='%f')#st.text_input("Sepal Length", "Type Here")
    
st.markdown("PerformanceRating:	1 'Low' 2 'Good' 3 'Excellent' 4 'Outstanding")   
result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
if st.button("RF Predict"):
	result = RFprediction(EmpDepartment, EmpJobRole, EmpEnvironmentSatisfaction, EmpLastSalaryHikePercent, EmpWorkLifeBalance, ExperienceYearsAtThisCompany, ExperienceYearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager)
st.success('The output is {}'.format(result))


#if st.button("XGB Predict"):
 #   result = XGBprediction(EmpDepartment, EmpJobRole, EmpEnvironmentSatisfaction, EmpLastSalaryHikePercent, EmpWorkLifeBalance, ExperienceYearsAtThisCompany, ExperienceYearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager)
#st.success('The output is {}'.format(result))
     
