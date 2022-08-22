import streamlit as st
import pandas as pd
import sys
import pickle


st.header("Rosmann Pharmaceutical Sales Prediction")

st.header("Distribution and Visualization of the pharmaceutical Data")

st.subheader("Correlation Analysis")
st.image('../images/corr.png')

st.subheader("Analysis of storetypes on open days")
st.image('../images/storetype.png')

st.subheader("State Holiday customer Analysis")
st.image('../images/stateholiday.png')

st.subheader("Assortment Effect On Sales")
st.image('../images/assortment.png')

st.subheader("Mean monthly sales")
st.image('../images/mean_monthly_sales.png')

st.subheader("AutoCorrelation")
st.image('../images/autocorr.png')

st.subheader("Partial AutoCorrelation")
st.image('../images/partial ac.png')

st.header("Model Analysis")

st.subheader("test and val loss plot")
st.image('../images/xloss.png')

st.subheader("Feature Importance on model")
st.image('../images/features.png')

st.subheader("Prediciton image - Time Series")
st.image('../images/lstm.png')