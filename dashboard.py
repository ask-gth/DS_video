import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load datasets from URLs
raw_data_path = "https://raw.githubusercontent.com/ask-gth/DS_video/refs/heads/main/raw_data.csv"
preprocessed_data_path = "https://raw.githubusercontent.com/ask-gth/DS_video/refs/heads/main/preprocessed_data.csv"

# Load data
raw_data = pd.read_csv(raw_data_path)
preprocessed_data = pd.read_csv(preprocessed_data_path)

# Sidebar Navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio(
    "Select a visualization:",
    (
        "Data Distribution",
        "Model Performance Metrics",
        "Feature Correlation (Preprocessed Data)",
        "Summary Statistics",
    )
)

# Title
st.title("Interactive Dashboard for Dementia Data Analysis")

# Data Distribution
if page == "Data Distribution":
    st.subheader("Data Distribution")
    
    # Distribution of Species Population (Raw Data)
    st.markdown("### Raw Data Distribution")
    fig_raw = px.histogram(raw_data, x='Species_Population', nbins=20, title="Raw Data Distribution")
    fig_raw.update_layout(yaxis_title="Count")
    st.plotly_chart(fig_raw)
    
    # Distribution of Species Population (Preprocessed Data)
    st.markdown("### Preprocessed Data Distribution")
    fig_cleaned = px.histogram(preprocessed_data, x='Species_Population', nbins=20, title="Preprocessed Data Distribution")
    fig_cleaned.update_layout(yaxis_title="Count")
    st.plotly_chart(fig_cleaned)

# Model Performance Metrics
elif page == "Model Performance Metrics":
    st.subheader("Model Performance Metrics Comparison")
    
    # Example metrics
    mse_raw, r2_raw = 31166.61, 0.84 
    mse_train, r2_train = 3116.05, 0.85  

    fig_metrics = go.Figure()
    fig_metrics.add_trace(go.Bar(
        name='MSE',
        x=['Raw Data', 'Preprocessed Data'],
        y=[mse_raw, mse_train]
    ))
    fig_metrics.add_trace(go.Bar(
        name='R²',
        x=['Raw Data', 'Preprocessed Data'],
        y=[r2_raw, r2_train]
    ))
    fig_metrics.update_layout(barmode='group', title="Model Performance Comparison")
    st.plotly_chart(fig_metrics)

# Feature Correlation (Preprocessed Data)
elif page == "Feature Correlation (Preprocessed Data)":
    st.subheader("Feature Correlation (Preprocessed Data)")
    
    # Select only numeric columns
    numeric_columns = preprocessed_data.select_dtypes(include=['float64', 'int64'])
    
    # Compute correlation matrix
    corr_matrix = numeric_columns.corr()
    
    # Heatmap
    fig_corr = px.imshow(
        corr_matrix,
        text_auto=True,
        title="Feature Correlation Matrix (Preprocessed Data)",
        color_continuous_scale="Viridis"
    )
    st.plotly_chart(fig_corr)

# Summary Statistics
elif page == "Summary Statistics":
    st.subheader("Summary Statistics")
    
    # Raw data summary
    st.markdown("### Raw Data Summary")
    st.write(raw_data.describe())
    
    # Preprocessed data summary
    st.markdown("### Preprocessed Data Summary")
    st.write(preprocessed_data.describe())
