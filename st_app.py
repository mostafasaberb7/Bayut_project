import joblib
import pandas as pd
import streamlit as st
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

# Load data and model
df2 = pd.read_csv('bayut_units_cleaned.csv')  # Assuming df2 is the cleaned dataset
model = joblib.load("model.pkl")

# Set Streamlit configuration
st.set_page_config("Real Estate Price Predictor", layout='wide')

def predict(area, rooms, property_type, city):
    # Make the prediction using the loaded model
    pred = model.predict([[area, rooms, property_type, city]])
    plots(round(pred[0], 2))

def home_page():
    # Display text
    st.title("DEPI Real Estate Predictor")
    st.header("Welcome to the Property Price Prediction Tool")
    st.subheader("This tool helps you estimate property prices.")

    st.markdown("**Use this tool to predict the price of real estate based on specific parameters.**")
    st.image('https://miro.medium.com/v2/resize:fit:640/format:webp/0*6odQHEjAdp40W2Nc.png', width=600)



def inputs():
    # Inputs for prediction
    st.title("Predict Property Price")
    
    area = st.number_input("Area (in sqft)",min_value=1)
    rooms = st.number_input("Number of Rooms", min_value=1, max_value=10)
    
    property_type = st.selectbox("Property Type", [[0,'Apartments'], [2,'Villas and Houses'], [1,'Vacation Properties']])
    city = st.selectbox("region", [[5,'القاهرة الجديدة'], [8,'المعادي'], [23,'مدينتي'], [20,'مدينة المستقبل'],
       [1,'العاصمة الإدارية الجديدة'], [22,'مدينة نصر'], [19,'مدينة الشروق'],
       [26,'هليوبوليس الجديدة'], [24,'مصر الجديدة'], [16,'شيراتون'], [9,'المقطم'], [0,'الزمالك'],
       [6,'القطامية'], [14,'زهراء المعادى'], [3,'العبور'], [7,'الماظة'], [27,'وسط القاهرة'],
       [4,'الفسطاط'], [11,'النزهة الجديدة'], [21,'مدينة بدر'], [15,'شبرا'], [17,'طرة'],
       [25,'مصر القديمة'], [10,'المنيل'], [13,'حدائق حلوان'], [18,'قصر النيل'], [2,'العباسية'],
       [12,'جاردن سيتي']])
    
    if st.button("Predict"):
        predict(area, rooms, property_type[0], city[0])

def plots(result=0):
    # Plotting the result and some visualizations
    st.title("Result")
    
    st.markdown(f"**Estimated Property Price: {result:,} EGP**")
    
    fig = plt.figure()
    sns.histplot(df2, x='Price')
    
    st.pyplot(fig)

    st.button("Make Another Prediction", on_click=inputs)

# Page Navigation
page = st.sidebar.selectbox("Select Page", ["Home", "Predict", "Plots"])

if page == 'Home':
    home_page()
elif page == 'Predict':
    inputs()
else:
    plots()

