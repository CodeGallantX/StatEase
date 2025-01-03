import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Project - StatEase",
    page_icon="🎯",
    layout="wide"
)

def calculate_stats_with_workings(class_intervals, frequencies):
    midpoints = [(interval[0] + interval[1]) / 2 for interval in class_intervals]
    f = np.array(frequencies)
    m = np.array(midpoints)

    n = f.sum()

    cumulative_f = np.cumsum(f)

    fm = f * m
    mean = np.sum(fm) / n
    deviation = m - mean
    deviation_squared = deviation ** 2
    fd_squared = f * deviation_squared

    mean_working = r"Mean = \frac{\sum fx}{\sum f}"
    mean_working += f" = \\frac{{{np.sum(fm)}}}{{{n}}} = {mean}"

    median_class = next(i for i, cf in enumerate(cumulative_f) if cf >= n / 2)
    L = class_intervals[median_class][0]
    F = cumulative_f[median_class - 1] if median_class > 0 else 0
    f_median = f[median_class]
    width = class_intervals[median_class][1] - class_intervals[median_class][0]
    median = L + (n / 2 - F) * width / f_median
    median_working = r"Median = L + \frac{\left(\frac{n}{2} - F\right) \times w}{f_{\text{median}}}"
    median_working += f" = {L} + \\frac{{({n}/2 - {F}) \cdot {width}}}{{{f_median}}} = {median}"

    mode_class = np.argmax(f)
    L_mode = class_intervals[mode_class][0]
    f_mode = f[mode_class]
    f_prev = f[mode_class - 1] if mode_class > 0 else 0
    f_next = f[mode_class + 1] if mode_class < len(f) - 1 else 0
    mode = L_mode + (f_mode - f_prev) / ((f_mode - f_prev) + (f_mode - f_next)) * width
    mode_working = r"Mode = L + \frac{(f_{\text{mode}} - f_{\text{prev}})}{(f_{\text{mode}} - f_{\text{prev}}) + (f_{\text{mode}} - f_{\text{next}})} \cdot w"
    mode_working += f" = {L_mode} + \\frac{{({f_mode} - {f_prev})}}{{({f_mode} - {f_prev}) + ({f_mode} - {f_next})}} \cdot {width} = {mode}"

    variance = np.sum(fd_squared) / n
    std_dev = np.sqrt(variance)

    cv = (std_dev / mean) * 100

    variance_working = r"Variance = \frac{\sum fd^2}{\sum f}"
    variance_working += f" = \\frac{{{np.sum(fd_squared)}}}{{{n}}} = {variance}"
    cv_working = r"CV = \frac{\text{Standard Deviation}}{\text{Mean}} \cdot 100"
    cv_working += f" = \\frac{{{std_dev}}}{{{mean}}} \cdot 100 = {cv}%"

    min_val = class_intervals[0][0]
    max_val = class_intervals[-1][1]

    min_working = f"Min = {min_val}"
    max_working = f"Max = {max_val}"

    lower_quartile = L + (n / 4 - F) * width / f_median
    upper_quartile = L + (3 * n / 4 - F) * width / f_median
    seventh_decile = L + (7 * n / 10 - F) * width / f_median
    eighty_third_percentile = L + (83 * n / 100 - F) * width / f_median

    quartile_working = r"Lower Quartile = L + \frac{\left(\frac{n}{4} - F\right) \cdot w}{f_{\text{median}}}"
    quartile_working += f" = {L} + \\frac{{({n}/4 - {F}) \cdot {width}}}{{{f_median}}} = {lower_quartile}"

    upper_quartile_working = r"Upper Quartile = L + \frac{\left(\frac{3n}{4} - F\right) \cdot w}{f_{\text{median}}}"
    upper_quartile_working += f" = {L} + \\frac{{({3 * n}/4 - {F}) \cdot {width}}}{{{f_median}}} = {upper_quartile}"

    decile_working = r"7^{th} \text{Decile} = L + \frac{\left(\frac{7n}{10} - F\right) \cdot w}{f_{\text{median}}}"
    decile_working += f" = {L} + \\frac{{({7 * n}/10 - {F}) \cdot {width}}}{{{f_median}}} = {seventh_decile}"

    percentile_working = r"83^{rd} \text{Percentile} = L + \frac{\left(\frac{83n}{100} - F\right) \cdot w}{f_{\text{median}}}"
    percentile_working += f" = {L} + \\frac{{({83 * n}/100 - {F}) \cdot {width}}}{{{f_median}}} = {eighty_third_percentile}"

    table_data = {
        'Class Interval': class_intervals,
        'Midpoint (m)': midpoints,
        'Frequency (f)': frequencies,
        'fm = f × m': fm,
        'Cumulative Frequency (cf)': cumulative_f,
        'Deviation(d) =  (m - mean)': deviation,
        'd² = (m - mean)²': deviation_squared,
        'fd² = f × (Deviation)²': fd_squared
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
        "mean_working": mean_working,
        "median_working": median_working,
        "mode_working": mode_working,
        "variance_working": variance_working,
        "cv_working": cv_working,
        "min_working": min_working,
        "max_working": max_working,
        "quartile_working": quartile_working,
        "upper_quartile_working": upper_quartile_working,
        "decile_working": decile_working,
        "percentile_working": percentile_working,
    }


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

if st.sidebar.button("Calculate Statistics", type="primary"):
    if len(class_intervals) == num_intervals and len(frequencies) == num_intervals:
        results = calculate_stats_with_workings(class_intervals, frequencies)

        st.subheader("Full Calculations and Workings")
        
        st.write("### Complete Table of Values")
        st.write(results["table"])

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

        st.markdown("### Variance and Coefficient of Variation")
        st.latex(results["variance_working"])
        st.latex(results["cv_working"])
        st.write(f"> Variance = {results['variance']}")
        st.write(f"> Coefficient of Variation (cv) = {results['cv']}%")
        st.write("---")

        st.markdown("### Minimum and Maximum Values")
        # st.write(results["min_working"])
        st.write(f"> Min = {results['min']}")
        # st.write(results["max_working"])
        st.write(f"> Max = {results['max']}")
        st.write("---")

        st.markdown("### Quartiles, Deciles, Percentiles")
        st.latex(results["quartile_working"])
        st.write(f"> Lower Quartile = {results['lower_quartile']}")
        st.latex(results["upper_quartile_working"])
        st.write(f"> Upper Quartile = {results['upper_quartile']}")
        st.latex(results["decile_working"])
        st.write(f"> 7th Decile = {results['seventh_decile']}")
        st.latex(results["percentile_working"])
        st.write(f"> 83rd Percentile = {results['eighty_third_percentile']}")
        st.write("---")
