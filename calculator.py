import streamlit as st
import numpy as np
# from scipy import stats
from streamlit_modal import Modal

def toggle_calculator():
    modal = Modal(key="calculator_modal", title="Advanced Calculator")

    if st.button("Open Calculator"):
        modal.open()

    if modal.is_open():
        with modal.container():
            st.write("## Advanced Statistical Calculator")

            calculation_type = st.selectbox(
                "Select the type of calculation:",
                ["Basic Arithmetic", "Statistics"]
            )

            if calculation_type == "Basic Arithmetic":
                numbers_input = st.text_area(
                    "Enter numbers (comma-separated):",
                    "1, 2, 3, 4, 5"
                )

                try:
                    numbers = [float(i) for i in numbers_input.split(",")]
                except ValueError:
                    st.error("Please enter valid numeric values.")
                    return

                if len(numbers) > 1:
                    operation = st.selectbox(
                        "Select an operation:", ["Addition", "Subtraction", "Multiplication", "Division"]
                    )

                    result = None
                    if st.button("Calculate", type="primary"):
                        if operation == "Addition":
                            result = sum(numbers)
                        elif operation == "Subtraction":
                            result = numbers[0]
                            for num in numbers[1:]:
                                result -= num
                        elif operation == "Multiplication":
                            result = np.prod(numbers)
                        elif operation == "Division":
                            result = numbers[0]
                            for num in numbers[1:]:
                                if num != 0:
                                    result /= num
                                else:
                                    st.error("Division by zero is not allowed!")
                                    break

                    if result is not None:
                        st.success(f"The result of {operation} is: {result}")
                else:
                    st.error("Please provide at least two numbers for arithmetic operations.")

            if calculation_type == "Statistics":
                data_input = st.text_area(
                    "Enter data values (comma-separated):",
                    "1, 2, 3, 4, 5"
                )

                try:
                    data = [float(i) for i in data_input.split(",")]
                except ValueError:
                    st.error("Please enter valid numeric values.")
                    return

                if len(data) > 1:
                    mean = np.mean(data)
                    median = np.median(data)
                    # mode = stats.mode(data)[0][0] 
                    std_dev = np.std(data)
                    variance = np.var(data)
                    sum_of_squares = np.sum(np.square(data))
                    with st.spinner("Calculating..."):
                        st.write(f"Mean: {mean:.2f}")
                        st.write(f"Median: {median:.2f}")
                        st.write(f"Mode: {mode:.2f}")
                        st.write(f"Standard Deviation: {std_dev:.2f}")
                        st.write(f"Variance: {variance:.2f}")
                        st.write(f"Sum of Squares: {sum_of_squares:.2f}")

                    if len(data) > 2:
                        st.write("If you have another list for correlation, please input it.")
                        y_input = st.text_area("Enter second data set for correlation (comma-separated):")
                        try:
                            y_data = [float(i) for i in y_input.split(",")]
                            if len(data) == len(y_data):
                                correlation = np.corrcoef(data, y_data)[0, 1]
                                st.write(f"Correlation Coefficient: {correlation:.2f}")
                            else:
                                st.error("The two data sets must have the same length.")
                        except ValueError:
                            st.warning("Please enter valid numeric values for the second data set.")

                    if len(data) >= 2:
                        x = np.array(range(1, len(data) + 1))
                        y = np.array(data)
                        # slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
                        st.write(f"Linear Regression - Slope: {slope:.2f}, Intercept: {intercept:.2f}")
                        st.write(f"R-squared value: {r_value**2:.2f}")

                else:
                    st.error("Please provide at least two data points for statistical calculations.")
