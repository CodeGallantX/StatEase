import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from manual_logic import calculate_statistics, plot_data


st.set_page_config(
    page_title="StatEase - Statistics Hub",
    page_icon="📊",
    layout="wide"
)


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700;1,900&family=Outfit:wght@100..900&display=swap');

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Merriweather', serif;
    }

    p, div, span, li, a {
        font-family: 'Outfit', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if "uploaded_data" not in st.session_state:
    st.session_state["uploaded_data"] = None
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Home" 

   
if "ungrouped_data" not in st.session_state:
    st.session_state.ungrouped_data = pd.DataFrame({"Data Points": [None] * 5})

if "grouped_data" not in st.session_state:
    st.session_state.grouped_data = pd.DataFrame(
        {"Class Interval": ["" for _ in range(5)], "Frequency": [None] * 5}
    )



st.title("📊 StatEase")
st.write("A user-friendly statistics app for descriptive analysis, visualizations, and more!")


st.sidebar.title("Menu")
options = st.sidebar.radio(
    "Choose a section:",
    ["Home", "Upload Dataset", "Descriptive Statistics", "Data Visualizations", "Manual Data Input"]
)
st.sidebar.markdown("_Made with ❤️ by_ [CodeGallantX](https://github.com/CodeGallantX)")

if options != st.session_state.current_page:
    st.session_state.current_page = options

if st.session_state.current_page == "Home":
    st.markdown("Get started by uploading dataset or manually inputting data values")
    upload_button = st.button("Open sidebar to Get Started")

    st.subheader("Welcome to StatEase!")
    st.write("""
        - Upload your dataset to begin statistical analysis.
        - Compute descriptive statistics and measures of central tendency.
        - Visualize your data with interactive charts and plots.
        - Manually input data for grouped or ungrouped frequency tables.
        - Future feature: Inferential statistics and hypothesis testing.
    """)



elif st.session_state.current_page == "Upload Dataset":
    st.subheader("Upload Your Dataset")
    uploaded_file = st.file_uploader("Upload your CSV or Excel file:", type=["csv", "xlsx"])

    if uploaded_file:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.session_state["uploaded_data"] = df

        st.write("**Preview of Uploaded Data**")
        st.dataframe(df.head())

        st.write("**Dataset Summary**")
        st.write(df.describe())

        st.write("**Missing Values**")
        st.write(df.isnull().sum())
    else:
        with open("student_performance.csv", "rb") as csv:
            st.info("Please upload a file to proceed or use sample dataset below")
            st.download_button(label="Download sample dataset", data=csv, file_name="student_performance.csv", mime="text/csv")

        
elif st.session_state.current_page == "Descriptive Statistics":
    st.subheader("Descriptive Statistics")

    if st.session_state["uploaded_data"] is None:
        st.warning("Please upload a dataset first in the 'Upload Dataset' section.")
    else:
        df = st.session_state["uploaded_data"]
        st.write("**Choose Columns for Analysis**")
        numeric_columns = df.select_dtypes(include=np.number).columns
        selected_columns = st.multiselect("Select numeric columns:", numeric_columns)

        if selected_columns:
            selected_data = df[selected_columns]
            st.write("**Summary Statistics**")
            st.write(selected_data.describe())

            # Measures of Central Tendency
            st.write("### Measures of Central Tendency")
            for col in selected_columns:
                st.write(f"#### {col}")
                total_sum = selected_data[col].sum()
                num_items = selected_data[col].count()
                mean = total_sum / num_items
                median = selected_data[col].median()
                mode = selected_data[col].mode()[0]

                # Display calculations for mean
                st.write(f"**Mean Calculation:**")
                st.latex(r"\text{Mean } \mu = \frac{\sum x}{n}")
                calculation = f"Mean = ({' + '.join(map(str, selected_data[col].dropna().tolist()))}) / {num_items} = {mean:.2f}"
                st.code(calculation, language="markdown")

                st.write(f"**Median:** {median:.2f}")
                st.write(f"**Mode:** {mode}")

            # Measures of Dispersion
            st.write("### Measures of Dispersion")
            for col in selected_columns:
                st.write(f"#### {col}")
                variance = selected_data[col].var()
                std_dev = selected_data[col].std()
                data_range = selected_data[col].max() - selected_data[col].min()

                # Display calculations for variance and standard deviation
                st.write(f"**Variance:** {variance:.2f}")
                st.write(f"**Standard Deviation:** {std_dev:.2f}")
                
                # Display calculation for range
                st.write(f"**Range Calculation:**")
                st.latex(r"\text{Range} = \text{Max} - \text{Min}")
                range_calculation = f"Range = {selected_data[col].max():.2f} - {selected_data[col].min():.2f} = {data_range:.2f}"
                st.code(range_calculation, language="markdown")

            # Copy-friendly output
            st.write("### Copy Workings")
            export_text = ""
            for col in selected_columns:
                total_sum = selected_data[col].sum()
                num_items = selected_data[col].count()
                mean = total_sum / num_items
                median = selected_data[col].median()
                mode = selected_data[col].mode()[0]
                variance = selected_data[col].var()
                std_dev = selected_data[col].std()
                data_range = selected_data[col].max() - selected_data[col].min()

                export_text += f"**{col}**:\n"
                export_text += f"- Mean: {mean:.2f} (Sum: {total_sum}, Count: {num_items})\n"
                export_text += f"- Median: {median:.2f}\n"
                export_text += f"- Mode: {mode}\n"
                export_text += f"- Variance: {variance:.2f}\n"
                export_text += f"- Standard Deviation: {std_dev:.2f}\n"
                export_text += f"- Range: {data_range:.2f} (Max: {selected_data[col].max():.2f}, Min: {selected_data[col].min():.2f})\n\n"

            st.text_area("Copy or Save Workings", export_text, height=200)

            # Optional download as file
            st.download_button(
                label="Download Calculations as Text File",
                data=export_text,
                file_name="descriptive_statistics.txt",
                mime="text/plain"
            )


elif st.session_state.current_page == "Data Visualizations":
    st.subheader("Data Visualizations")

    if st.session_state["uploaded_data"] is None:
        st.warning("Please upload a dataset first in the 'Upload Dataset' section.")
    else:
        df = st.session_state["uploaded_data"]
        st.write("**Choose Columns for Visualization**")
        all_columns = df.columns
        selected_columns = st.multiselect("Select columns to visualize:", all_columns)

        if selected_columns:
            st.write("**Available Plots**")
            plot_type = st.selectbox("Select a plot type:", ["Histogram", "Boxplot", "Scatter Plot"])

            if plot_type == "Histogram":
                for col in selected_columns:
                    st.write(f"**Histogram for {col}**")
                    plt.figure(figsize=(8, 4))
                    sns.histplot(df[col], kde=True, bins=20, color="skyblue")
                    st.pyplot(plt)

            elif plot_type == "Boxplot":
                for col in selected_columns:
                    st.write(f"**Boxplot for {col}**")
                    plt.figure(figsize=(8, 4))
                    sns.boxplot(y=df[col], color="orange")
                    st.pyplot(plt)

            elif plot_type == "Scatter Plot":
                if len(selected_columns) < 2:
                    st.warning("Please select at least two columns for a scatter plot.")
                else:
                    x_axis = st.selectbox("Select X-axis:", selected_columns)
                    y_axis = st.selectbox("Select Y-axis:", selected_columns)

                    st.write(f"**Scatter Plot: {x_axis} vs {y_axis}**")
                    plt.figure(figsize=(8, 4))
                    sns.scatterplot(x=df[x_axis], y=df[y_axis], color="green")
                    st.pyplot(plt)



# Manual Data Input Section
elif st.session_state.current_page == "Manual Data Input":
    st.subheader("Manual Data Input")
    input_type = st.radio("Choose Data Input Type:", ["Ungrouped Data", "Grouped Data"])

    if input_type == "Ungrouped Data":
        st.write("### Step 1: Enter ungrouped data points:")
        st.write("Ungrouped data consists of individual data points without grouping into intervals.")
        
        # Edit table for ungrouped data
        st.session_state.ungrouped_data = st.data_editor(
            st.session_state.ungrouped_data, num_rows="dynamic"
        )
        
        # Ensure Data Points are numeric
        st.session_state.ungrouped_data["Data Points"] = pd.to_numeric(st.session_state.ungrouped_data["Data Points"], errors='coerce')

        # Derived fields
        st.write("### Step 2: Optional Derived Fields (e.g., Cumulative Frequency, x², fx², fx)")
        if st.button("Add Cumulative Frequency"):
            st.session_state.ungrouped_data["Cumulative Frequency"] = st.session_state.ungrouped_data["Data Points"].cumsum()

        if st.button("Add fx (Data Points × Frequency)"):
            st.session_state.ungrouped_data["fx"] = st.session_state.ungrouped_data["Data Points"] * st.session_state.ungrouped_data["Data Points"]

        if st.button("Add x² (Square of Data Points)"):
            st.session_state.ungrouped_data["x²"] = st.session_state.ungrouped_data["Data Points"] ** 2
        
        if st.button("Add fx² (Data Points × x²)"):
            st.session_state.ungrouped_data["fx²"] = st.session_state.ungrouped_data["Data Points"] * st.session_state.ungrouped_data["x²"]

        st.write("### Step 3: Descriptive Statistics")
        data_points = st.session_state.ungrouped_data["Data Points"].dropna()
        if len(data_points) > 0:
            mean, median, mode, std_dev, variance = calculate_statistics(data_points)
            st.write(f"**Mean**: {mean}")
            st.write(f"**Median**: {median}")
            st.write(f"**Mode**: {mode}")
            st.write(f"**Standard Deviation**: {std_dev}")
            st.write(f"**Variance**: {variance}")

        if len(data_points) > 0:
            plot_data(data_points)

        st.write("### Step 4: View the Data")
        st.write("**Entered Data (with optional derived fields):**")
        st.write(st.session_state.ungrouped_data.dropna().reset_index(drop=True))

    elif input_type == "Grouped Data":
        st.write("### Step 1: Enter grouped data (Class Intervals and Frequency):")
        st.write("Grouped data consists of ranges (class intervals) and corresponding frequencies.")
        
        st.session_state.grouped_data = st.data_editor(
            st.session_state.grouped_data, num_rows="dynamic"
        )
        
        st.session_state.grouped_data["Frequency"] = pd.to_numeric(st.session_state.grouped_data["Frequency"], errors='coerce')

        st.write("### Step 2: Optional Derived Fields (e.g., Cumulative Frequency, x², fx², fx)")
        if st.button("Add Cumulative Frequency"):
            st.session_state.grouped_data["Cumulative Frequency"] = st.session_state.grouped_data["Frequency"].cumsum()
        
        if st.button("Add x² (Square of Midpoint)"):
            st.session_state.grouped_data["Midpoint"] = (
                st.session_state.grouped_data["Class Interval"].apply(lambda x: int(x.split('-')[0])) +
                st.session_state.grouped_data["Class Interval"].apply(lambda x: int(x.split('-')[1]))
            ) / 2
            st.session_state.grouped_data["x²"] = st.session_state.grouped_data["Midpoint"] ** 2

        if "x²" in st.session_state.grouped_data.columns:
            if st.button("Add fx² (Frequency * x²)"):
                st.session_state.grouped_data["fx²"] = st.session_state.grouped_data["Frequency"] * st.session_state.grouped_data["x²"]

        if st.button("Add fx (Frequency * Midpoint)"):
            st.session_state.grouped_data["fx"] = st.session_state.grouped_data["Frequency"] * st.session_state.grouped_data["Midpoint"]

        st.write("### Step 3: Descriptive Statistics and Visualization")
        if len(st.session_state.grouped_data["Frequency"].dropna()) > 0:
            grouped_data = st.session_state.grouped_data["Frequency"].dropna()
            plot_data(grouped_data)

        st.write("### Step 4: View the Data")
        st.write("**Grouped Frequency Table (with optional derived fields):**")
        st.write(st.session_state.grouped_data.dropna().reset_index(drop=True))