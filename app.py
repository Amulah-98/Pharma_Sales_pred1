from distutils.command.install_egg_info import safe_name
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('ideal_model1.pkl', 'rb') 
ideal_model1 = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Open, DayOfWeek, Promo, Sales):   
    

    # Pre-processing user input    
    if Open == "Yes":
        Open = 1
    else:
        Open = 0
 
    if Promo == "1":
        Promo = 1
    else:
        Promo = 0


    if (DayOfWeek=='1'):
        DayOfWeek = 1
    elif (DayOfWeek=='2'):
        DayOfWeek = 2
    elif (DayOfWeek=='3'):
        DayOfWeek = 3
    elif (DayOfWeek=='4'):
        DayOfWeek = 4
    elif (DayOfWeek=='5'):
        DayOfWeek = 5
    elif (DayOfWeek=='6'):
        DayOfWeek = 6
    elif (DayOfWeek=='7'):
        DayOfWeek = 7
    else:
        print("Wrong Input!!!!!")
        
    

    # Making predictions 
    prediction = ideal_model1.predict( 
        [[Open, DayOfWeek, Promo]])
        
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred
    
    
    
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
   
    # display the front end aspect
    st.markdown('Streamlit Sales Prediction ML App', unsafe_allow_html = True) #any HTML tags found in the body will be escaped and therefore treated as pure text. This behavior may be turned off by setting this argument to True. 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Open = st.selectbox('Open',("Yes","No"))
    Promo = st.selectbox('Promo',("0","1")) 
    DayOfWeek = st.selectbox('Day Of Week', ("1","2","3","4","5","6","7")) 
    Sales =  'Sales'
    result =""

    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Open, DayOfWeek, Promo, Sales) 
        st.success('Your sales is {}'.format(result))
        print(Sales)
     
if __name__=='__main__': 
    main()