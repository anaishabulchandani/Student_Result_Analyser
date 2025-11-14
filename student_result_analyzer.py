import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Student Result Analyzer")

# Initialize student data
if "students" not in st.session_state:
    st.session_state.students = pd.DataFrame(
        columns=["Name", "Roll No", "Maths", "Science", "English", "Computer", "Average"]
    )

# Sidebar Menu
menu = st.sidebar.radio(
    " Menu",
    [
        "Add Student Record",
        "Display All Records",
        "Search Student",
        "Sort Records by Average",
        "Show Topper",
        "Show Class Average",
        "Show Graph (Bar Chart)",
        "Exit",
    ],
)

# Add Student Record
if menu.startswith("1"):
    st.subheader("Add Student Record")
    name = st.text_input("Enter Student Name")
    roll = st.text_input("Enter Roll No")
    maths = st.number_input("Maths Marks", min_value=0, max_value=100, step=1)
    science = st.number_input("Science Marks", min_value=0, max_value=100, step=1)
    english = st.number_input("English Marks", min_value=0, max_value=100, step=1)
    computer = st.number_input("Computer Marks", min_value=0, max_value=100, step=1)

    if st.button("Add Record"):
        if name and roll:
            avg = (maths + science + english + computer) / 4
            new_data = pd.DataFrame(
                {
                    "Name": [name],
                    "Roll No": [roll],
                    "Maths": [maths],
                    "Science": [science],
                    "English": [english],
                    "Computer": [computer],
                    "Average": [avg],
                }
            )
            st.session_state.students = pd.concat([st.session_state.students, new_data], ignore_index=True)
            st.success(f"Record Added for {name} (Average: {avg:.2f}%)")
        else:
            st.error(" Please enter both name and roll number!")

# 2️ Display All Records
elif menu.startswith("2"):
    st.subheader("All Student Records")
    if not st.session_state.students.empty:
        st.dataframe(st.session_state.students)
    else:
        st.info("No records found yet!")

# 3️ Search Student (Linear Search)
elif menu.startswith("3"):
    st.subheader("Search Student by Roll No")
    roll = st.text_input("Enter Roll No to Search")
    if st.button("Search"):
        found = False
        for _, row in st.session_state.students.iterrows():
            if row["Roll No"] == roll:
                st.success(f"Found: {row['Name']}")
                st.write(row)
                found = True
                break
        if not found:
            st.warning("No student found with that Roll No.")

# 4️ Sort Records by Average (Bubble Sort)
elif menu.startswith("4"):
    st.subheader("Sort Records by Average Marks")
    df = st.session_state.students.copy()
    if df.empty:
        st.info("No data to sort.")
    else:
        n = len(df)
        for i in range(n):
            for j in range(0, n - i - 1):
                if df.loc[j, "Average"] < df.loc[j + 1, "Average"]:
                    df.iloc[[j, j + 1]] = df.iloc[[j + 1, j]].values
        st.dataframe(df)

# 5 Show Topper
elif menu.startswith("5"):
    st.subheader("Topper of the Class")
    if not st.session_state.students.empty:
        topper = st.session_state.students.loc[st.session_state.students["Average"].idxmax()]
        st.success(f"Topper: {topper['Name']} ({topper['Average']:.2f}%)")
        st.write(topper)
    else:
        st.info("No data available yet.")

# 6️ Show Class Average
elif menu.startswith("6"):
    st.subheader("Class Average")
    if not st.session_state.students.empty:
        avg = st.session_state.students["Average"].mean()
        st.success(f"Class Average: {avg:.2f}%")
    else:
        st.info("No records yet!")

# 7️ Show Graph (Bar Chart)
elif menu.startswith("7"):
    st.subheader("Bar Chart of Student Averages")
    if not st.session_state.students.empty:
        fig, ax = plt.subplots()
        ax.bar(st.session_state.students["Name"], st.session_state.students["Average"], color="skyblue")
        plt.xticks(rotation=45)
        plt.ylabel("Average Percentage")
        plt.title("Student Performance")
        st.pyplot(fig)
    else:
        st.info("No data to plot yet.")

# 8️ Exit
elif menu.startswith("8"):
    st.subheader("Thank you for using Student Result Analyzer!")
