import streamlit as st
import pandas as pd

def main():
    # Title
    st.title("🎓 Student Management System")

    # Initialize session state for storing student data
    if "students" not in st.session_state:
        st.session_state.students = pd.DataFrame(columns=["Name", "Roll No", "Marks"])

    # Sidebar menu
    menu = st.sidebar.selectbox("Menu", ["Add Student", "View Students", "Search Student", "Find Topper"])

    # Add student
    if menu == "Add Student":
        st.subheader("Add New Student")
        name = st.text_input("Enter Student Name")
        roll = st.text_input("Enter Roll No")
        marks = st.number_input("Enter Marks", min_value=0, max_value=100)

        if st.button("Add"):
            new_student = pd.DataFrame({"Name": [name], "Roll No": [roll], "Marks": [marks]})
            st.session_state.students = pd.concat([st.session_state.students, new_student], ignore_index=True)
            st.success(f"Student {name} added successfully!")

    # View all students
    elif menu == "View Students":
        st.subheader("All Student Records")
        if not st.session_state.students.empty:
            st.dataframe(st.session_state.students)
        else:
            st.info("No records found.")

    # Search student
    elif menu == "Search Student":
        st.subheader("Search by Roll No")
        roll = st.text_input("Enter Roll No to Search")
        if st.button("Search"):
            result = st.session_state.students[st.session_state.students["Roll No"] == roll]
            if not result.empty:
                st.table(result)
            else:
                st.warning("No student found with that Roll No.")

    # Find topper
    elif menu == "Find Topper":
        st.subheader("Topper of the Class")
        if not st.session_state.students.empty:
            topper = st.session_state.students.loc[st.session_state.students["Marks"].idxmax()]
            st.success(f"🏆 Topper: {topper['Name']} (Marks: {topper['Marks']})")
        else:
            st.info("No data available yet.")

if __name__ == "__main__":
    main()
