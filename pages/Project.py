import streamlit as st
import pandas as pd
import numpy as np
from calculator import toggle_calculator

st.set_page_config(
    page_title="Project - StatEase",
    page_icon="🎯",
    layout="wide"
)

# toggle_calculator()

def calculate_stats_with_workings(class_intervals, frequencies, assumed_mean=None):
    midpoints = [(interval[0] + interval[1]) / 2 for interval in class_intervals]
    f = np.array(frequencies)
    m = np.array(midpoints)
    n = f.sum()

    cumulative_f = np.cumsum(f)

    # Compute the mean
    if assumed_mean is not None:
        deviation = m - assumed_mean
        fm = f * deviation
        mean = assumed_mean + np.sum(fm) / n
        mean_working = (
            r"Mean = A + \frac{\sum f(m - A)}{\sum f}"
            f" = {assumed_mean} + \\frac{{{np.sum(fm)}}}{{{n}}} = {mean}"
        )
    else:
        fm = f * m
        mean = np.sum(fm) / n
        deviation = m - mean
        mean_working = (
            r"Mean = \frac{\sum fx}{\sum f}"
            f" = \\frac{{{np.sum(fm)}}}{{{n}}} = {mean}"
        )

    # Compute other values
    fd = f * deviation
    deviation_squared = deviation ** 2
    fd_squared = f * deviation_squared

    # Median Calculation
    median_class = next(i for i, cf in enumerate(cumulative_f) if cf >= n / 2)
    L = class_intervals[median_class][0]- 0.5
    F = cumulative_f[median_class - 1] if median_class > 0 else 0
    f_median = f[median_class]
    width = class_intervals[median_class][1] - class_intervals[median_class][0]
    median = L + (n / 2 - F) * width / f_median
    median_working = (
        r"Median = L + \frac{\left(\frac{n}{2} - F\right) \cdot w}{f_{\text{median}}}"
        f" = {L} + \\frac{{({n}/2 - {F}) \cdot {width}}}{{{f_median}}} = {median}"
    )

    # Mode Calculation
    mode_class = np.argmax(f)
    L_mode = class_intervals[mode_class][0]
    f_mode = f[mode_class]
    f_prev = f[mode_class - 1] if mode_class > 0 else 0
    f_next = f[mode_class + 1] if mode_class < len(f) - 1 else 0
    mode = L_mode + (f_mode - f_prev) / ((f_mode - f_prev) + (f_mode - f_next)) * width
    mode_working = (
        r"Mode = L + \frac{(f_{\text{mode}} - f_{\text{prev}})}{(f_{\text{mode}} - f_{\text{prev}}) + (f_{\text{mode}} - f_{\text{next}})} \cdot w"
        f" = {L_mode} + \\frac{{({f_mode} - {f_prev})}}{{({f_mode} - {f_prev}) + ({f_mode} - {f_next})}} \cdot {width} = {mode}"
    )

    # Variance and Standard Deviation
    variance = np.sum(fd_squared) / n
    std_dev = np.sqrt(variance)
    variance_working = (
        r"Variance = \frac{\sum f(m - \text{mean})^2}{\sum f}"
        f" = \\frac{{{np.sum(fd_squared)}}}{{{n}}} = {variance}"
    )
    cv = (std_dev / mean) * 100
    cv_working = (
        r"CV = \frac{\text{Standard Deviation}}{\text{Mean}} \times 100 = \frac{" 
        f"{std_dev}{{{mean}}} \times 100 = {cv}%"
    )

    # Quartiles, Deciles, Percentiles
    lower_quartile = L + (n / 4 - F) * width / f_median
    upper_quartile = L + (3 * n / 4 - F) * width / f_median
    seventh_decile = L + (7 * n / 10 - F) * width / f_median
    eighty_third_percentile = L + (83 * n / 100 - F) * width / f_median

    quartile_working = (
        r"Lower Quartile = L + \frac{\left(\frac{n}{4} - F\right) \cdot w}{f_{\text{median}}}"
        f" = {L} + \\frac{{({n}/4 - {F}) \cdot {width}}}{{{f_median}}} = {lower_quartile}"
    )
    upper_quartile_working = (
        r"Upper Quartile = L + \frac{\left(\frac{3n}{4} - F\right) \cdot w}{f_{\text{median}}}"
        f" = {L} + \\frac{{({3 * n}/4 - {F}) \cdot {width}}}{{{f_median}}} = {upper_quartile}"
    )
    seventh_decile_working = (
        r"7th Decile = L + \frac{\left(\frac{7n}{10} - F\right) \cdot w}{f_{\text{median}}}"
        f" = {L} + \\frac{{({7 * n}/10 - {F}) \cdot {width}}}{{{f_median}}} = {seventh_decile}"
    )
    eighty_third_percentile_working = (
        r"83rd Percentile = L + \frac{\left(\frac{83n}{100} - F\right) \cdot w}{f_{\text{median}}}"
        f" = {L} + \\frac{{({83 * n}/100 - {F}) \cdot {width}}}{{{f_median}}} = {eighty_third_percentile}"
    )

    min_val = class_intervals[0][0]
    max_val = class_intervals[-1][1]

    table_data = {
        'Class Interval': class_intervals,
        'class mark (x)': midpoints,
        'Frequency (f)': frequencies,
        'fx': fm,
        'Cumulative Frequency (cf)': cumulative_f,
        'd = (x - x̄ or A)': deviation,
        'fd': fd,
        'd²': deviation_squared,
        'fd²': fd_squared,
    }

    df = pd.DataFrame(table_data)

    return {
        "table": df,
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": variance,
        "std_dev": std_dev,
        "cv": cv,
        "min": min_val,
        "max": max_val,
        "lower_quartile": lower_quartile,
        "upper_quartile": upper_quartile,
        "seventh_decile": seventh_decile,
        "eighty_third_percentile": eighty_third_percentile,
        "variance_working": variance_working,
        "cv_working": cv_working,
        "quartile_working": quartile_working,
        "upper_quartile_working": upper_quartile_working,
        "seventh_decile_working": seventh_decile_working,
        "eighty_third_percentile_working": eighty_third_percentile_working,
        "mean_working": mean_working,
        "median_working": median_working,
        "mode_working": mode_working,
    }

# Streamlit page title and layout
st.title("STA111: Statistics Project")
st.write("This page is for the STA111 project and will guide you in completing your statistical calculations.")
st.button("Open the sidebar to get started", type="primary")

st.sidebar.header("Input Data")
num_intervals = st.sidebar.number_input("Number of class intervals", min_value=1, step=1, value=5)

st.sidebar.subheader("Class Intervals")
class_intervals = []
for i in range(num_intervals):
    interval = st.sidebar.text_input(f"Interval {i + 1} (e.g., '50-59'):", key=f"interval_{i}")
    if interval:
        try:
            class_intervals.append([float(x) for x in interval.split("-")])
        except ValueError:
            st.sidebar.error("Invalid format. Use 'a-b' (e.g., 50-59).")

st.sidebar.subheader("Frequencies")
frequencies = []
for i in range(num_intervals):
    freq = st.sidebar.number_input(f"Frequency for Interval {i + 1}:", min_value=0, step=1, value=0, key=f"freq_{i}")
    frequencies.append(freq)

assumed_mean = st.sidebar.number_input(
    "Assumed Mean (Optional, leave blank for normal mean):", value=None, step=0.1, format="%.2f"
)

if st.sidebar.button("Calculate Statistics", type="primary"):
    if len(class_intervals) == num_intervals and len(frequencies) == num_intervals:
        results = calculate_stats_with_workings(class_intervals, frequencies, assumed_mean)

        st.subheader("Full Calculations and Workings")
        st.write("### Complete Table of Values")
        st.write(results["table"])

        # Display workings in LaTeX format
        st.markdown("### Mean")
        st.latex(results["mean_working"])
        st.write(f"> Mean = {results['mean']}")
        st.write("---")

        st.markdown("### Median")
        st.latex(results["median_working"])
        st.write(f"> Median = {results['median']}")
        st.write("---")

        st.markdown("### Mode")
        st.latex(results["mode_working"])
        st.write(f"> Mode = {results['mode']}")
        st.write("---")

        st.markdown("### Variance")
        st.latex(results["variance_working"])
        st.write(f"> Variance = {results['variance']}")
        st.write("---")

        st.markdown("### Coefficient of Variation (CV)")
        st.write(results["cv_working"])
        st.write(f"> CV = {results['cv']}%")
        st.write("---")

        st.markdown("### Quartiles")
        st.latex(results["quartile_working"])
        st.write(f"> Lower Quartile = {results['lower_quartile']}")
        st.latex(results["upper_quartile_working"])
        st.write(f"> Upper Quartile = {results['upper_quartile']}")
        st.write("---")

        st.markdown("### Deciles and Percentiles")
        st.latex(results["seventh_decile_working"])
        st.write(f"> 7th Decile = {results['seventh_decile']}")
        st.latex(results["eighty_third_percentile_working"])
        st.write(f"> 83rd Percentile = {results['eighty_third_percentile']}")
        st.write("---")

        st.markdown("### Minimum and Maximum Values")
        st.write(f"> Min = {results['min']}")
        st.write(f"> Max = {results['max']}")
        st.write("---")
