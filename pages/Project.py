import streamlit as st
import pandas as pd
import numpy as np

# Functions for calculations
def calculate_stats(class_intervals, frequencies):
    # Calculating class midpoints
    midpoints = [(interval[0] + interval[1]) / 2 for interval in class_intervals]
    f = np.array(frequencies)
    m = np.array(midpoints)

    # Total frequency
    n = f.sum()

    # Mean
    mean = np.sum(f * m) / n

    # Median
    cumulative_f = np.cumsum(f)
    median_class = next(i for i, cf in enumerate(cumulative_f) if cf >= n / 2)
    L = class_intervals[median_class][0]  # Lower boundary of median class
    F = cumulative_f[median_class - 1] if median_class > 0 else 0  # Cumulative frequency before median class
    f_median = f[median_class]  # Frequency of median class
    width = class_intervals[median_class][1] - class_intervals[median_class][0]  # Class width
    median = L + (n / 2 - F) * width / f_median

    # Mode
    mode_class = np.argmax(f)
    L_mode = class_intervals[mode_class][0]
    f_mode = f[mode_class]
    f_prev = f[mode_class - 1] if mode_class > 0 else 0
    f_next = f[mode_class + 1] if mode_class < len(f) - 1 else 0
    mode = L_mode + (f_mode - f_prev) / ((f_mode - f_prev) + (f_mode - f_next)) * width

    # Lower and Upper Quartiles
    lower_quartile = L + (n / 4 - F) * width / f_median
    upper_quartile = L + (3 * n / 4 - F) * width / f_median

    # Variance
    variance = np.sum(f * (m - mean) ** 2) / n

    # Coefficient of Variation
    std_dev = np.sqrt(variance)
    cv = (std_dev / mean) * 100

    # Deciles and Percentiles
    seventh_decile = L + (7 * n / 10 - F) * width / f_median
    eighty_third_percentile = L + (83 * n / 100 - F) * width / f_median

    # Intermediate table
    data = {
        "Class Interval": [f"{int(interval[0])}-{int(interval[1])}" for interval in class_intervals],
        "Midpoint (m)": midpoints,
        "Frequency (f)": frequencies,
        "f * m": f * m,
        "Cumulative Frequency (CF)": cumulative_f,
    }
    table = pd.DataFrame(data)

    return {
        "table": table,
        "mean": mean,
        "median": median,
        "mode": mode,
        "lower_quartile": lower_quartile,
        "upper_quartile": upper_quartile,
        "variance": variance,
        "cv": cv,
        "seventh_decile": seventh_decile,
        "eighty_third_percentile": eighty_third_percentile,
    }

# Streamlit UI
st.title("Statistics Calculator for Grouped Data")
st.write("Enter class intervals, frequencies, and other details to compute statistical measures.")

# Input class intervals
st.subheader("Input Class Intervals")
num_intervals = st.number_input("Number of class intervals", min_value=1, step=1, value=5)

class_intervals = []
for i in range(num_intervals):
    interval = st.text_input(f"Enter interval {i + 1} (e.g., '50-59'):", key=f"interval_{i}")
    if interval:
        try:
            class_intervals.append([float(x) for x in interval.split("-")])
        except ValueError:
            st.error("Invalid format. Please enter intervals as 'a-b' (e.g., 50-59).")

# Input frequencies
st.subheader("Input Frequencies")
frequencies = []
for i in range(num_intervals):
    freq = st.number_input(f"Enter frequency for interval {class_intervals[i] if i < len(class_intervals) else 'Interval'}:", 
                           min_value=0, step=1, value=0, key=f"freq_{i}")
    frequencies.append(freq)

# Calculate and display statistics
if st.button("Calculate Statistics"):
    if len(class_intervals) == num_intervals and len(frequencies) == num_intervals:
        results = calculate_stats(class_intervals, frequencies)

        # Display intermediate table
        st.subheader("Intermediate Table")
        st.dataframe(results["table"])

        # Display statistics
        st.subheader("Calculated Statistics")
        for key, value in results.items():
            if key != "table":
                st.write(f"{key.replace('_', ' ').capitalize()}: {value:.2f}")
    else:
        st.error("Please fill in all class intervals and frequencies correctly.")

# Formula explanation
st.subheader("Quartile Coefficient of Deviation")
st.write("The Quartile Coefficient of Deviation is given by:")
st.latex(r"\text{QCD} = \frac{Q3 - Q1}{Q3 + Q1}")
