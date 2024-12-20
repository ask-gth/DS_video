import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load datasets
raw_data = pd.read_csv('raw_data.csv')
preprocessed_data = pd.read_csv('preprocessed_data.csv')

# Sidebar: Select visualization
st.sidebar.header("Visualization Options")
visualization = st.sidebar.selectbox(
    "Choose a visualization",
    [
        "Data Distribution",
        "Model Performance Metrics",
        "Feature Correlation (Preprocessed Data)",
        "Summary Statistics"
    ]
)

# Title
st.title("Interactive Dashboard for Reserve Data Analysis")

# Data Distribution
if visualization == "Data Distribution":
    st.subheader("Data Distribution")
    
    # Distribution of Species Population (Raw Data)
    st.markdown("### Raw Data Distribution")
    fig_raw = px.histogram(raw_data, x='Species_Population', nbins=20, title="Raw Data Distribution")
    fig_raw.update_layout(yaxis_title="Reserves Count")
    st.plotly_chart(fig_raw)
    
    # Distribution of Species Population (Preprocessed Data)
    st.markdown("### Preprocessed Data Distribution")
    fig_cleaned = px.histogram(preprocessed_data, x='Species_Population', nbins=20, title="Preprocessed Data Distribution")
    fig_cleaned.update_layout(yaxis_title="Reserves Count")
    st.plotly_chart(fig_cleaned)

# Model Performance Metrics
elif visualization == "Model Performance Metrics":
    st.subheader("Model Performance Metrics Comparison")
    
    # Example metrics
    mse_raw, r2_raw = 200.0, 0.75  # Replace with actual computed metrics
    mse_train, r2_train = 150.0, 0.85  # Replace with actual computed metrics

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
elif visualization == "Feature Correlation (Preprocessed Data)":
    st.subheader("Feature Correlation (Preprocessed Data)")
    
    # Compute correlation matrix
    corr_matrix = preprocessed_data.corr()
    
    # Heatmap
    fig_corr = px.imshow(
        corr_matrix,
        text_auto=True,
        title="Feature Correlation Matrix (Preprocessed Data)",
        color_continuous_scale="Viridis"
    )
    st.plotly_chart(fig_corr)

# Summary Statistics
elif visualization == "Summary Statistics":
    st.subheader("Summary Statistics")
    
    # Raw data summary
    st.markdown("### Raw Data Summary")
    st.write(raw_data.describe())
    
    # Preprocessed data summary
    st.markdown("### Preprocessed Data Summary")
    st.write(preprocessed_data.describe())
