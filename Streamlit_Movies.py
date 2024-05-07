import streamlit as st
import pickle

# Load the model
with open('/Users/sridharkandi/Downloads/optimized_svd_model.pkl','rb') as file:
    model=pickle.load(file)

# Title
st.title('Movie Recommendation System')

#input fields
user_id=st.number_input('Enter User ID',min_value=1,value=1)
movie_id=st.number_input('Enter Movie ID',min_value=1,value=1)

# Button to make prediction
if st.button('Predict Rating'):
    #Assuming the model has a predict method that takes user ID and movie ID
    prediction=model.predict(user_id,movie_id)
    #Extracting the estimated rating from the prediction object
    estimated_rating=int(prediction.est)

    #Define a dictionary to map ratings to descriptive messages
    rating_messages={
        1: "Might be worth a try",
        2: "Decent watch",
        3: "Good choice",
        4: "Highly recommended",
        5: "Must watch"
    }

    #Get the descriptive message based on the rating
    message=rating_messages.get(estimated_rating,"Rating out of bounds")

    st.write(f'Predicted Rating:{estimated_rating}-{message}')
else:
    st.write('Enter values to predict the rating.')
