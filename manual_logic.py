import streamlit as st
import matplotlib.pyplot as plt

def calculate_statistics(data):
    mean = data.mean()
    median = data.median()
    mode = data.mode().values[0]
    std_dev = data.std()
    variance = data.var()
    return mean, median, mode, std_dev, variance

def plot_data(data):
    st.subheader("Data Visualization")
    
    # Histogram for ungrouped data
    if data.ndim == 1:
        fig, ax = plt.subplots()
        ax.hist(data, bins=10, edgecolor='black')
        ax.set_title("Histogram")
        ax.set_xlabel("Data Points")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)
    
    else:
        st.write("Grouped data visualization not yet supported.")