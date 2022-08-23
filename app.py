import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('ideal_model.pkl', 'rb') 
ideal_model = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Open, DayOfWeek, Promo):   
 
    # Pre-processing user input    
    if Open == "Open":
        Open = 1
    else:
        Open = 0
 
    if Promo == "1":
        Promo = 1
    else:
        Promo = 0


    if (DayOfWeek==1):
        print(DayOfWeek," is Sunday")
    elif (DayOfWeek==2):
        print(DayOfWeek," is Monday")
    elif (DayOfWeek==3):
        print(DayOfWeek," is Tuesday")
    elif (DayOfWeek==4):
        print(DayOfWeek," is Wednesday")
    elif (DayOfWeek==5):
        print(DayOfWeek," is Thursday")
    elif (DayOfWeek==6):
        print(DayOfWeek," is Friday")
    elif (DayOfWeek==7):
        print(DayOfWeek," is Saturday")
    else:
        print("Wrong Input!!!!!")
 
  
 
    # Making predictions 
    prediction = ideal_model.predict( 
        [[Open, DayOfWeek, Promo]])
    
    Sales = Sales.prediction

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
    DayOfWeek = st.number_input("Day Of Week") 
    Sales = st.number_input("Total Sales")
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Open, DayOfWeek, Promo) 
        st.success('Your sales is {}'.format(result))
        print(Sales)
     
if __name__=='__main__': 
    main()