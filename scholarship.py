import streamlit as st
import pandas as pd

def load_scholarship_data():
    # Load the scholarships data from a CSV file
    scholarships = pd.read_csv('scholarships.csv')
    return scholarships

def scholarship_finder():
    st.title("Scholarship Finder")
    st.write("Find scholarships based on your qualifications and interests.")

    # Load scholarship data
    scholarships = load_scholarship_data()

    # User inputs for qualifications and interests
    qualification = st.selectbox("Select Your Qualification", options=scholarships['Qualification'].unique())
    interest = st.selectbox("Select Your Interest", options=scholarships['Interest'].unique())

    if st.button("Find Scholarships"):
        # Filter scholarships based on user inputs
        filtered_scholarships = scholarships[
            (scholarships['Qualification'] == qualification) & 
            (scholarships['Interest'] == interest)
        ]

        if not filtered_scholarships.empty:
            st.write("### Scholarships Found:")
            for index, row in filtered_scholarships.iterrows():
                st.write(f"**Name:** {row['Name']}")
                st.write(f"**Qualification:** {row['Qualification']}")
                st.write(f"**Interest:** {row['Interest']}")
                st.write(f"**Deadline:** {row['Deadline']}")
                st.write(f"**Application Tips:** {row['Application_Tips']}")
                st.write("---")
        else:
            st.write("No scholarships found for your selected qualifications and interests.")

def load_career_data():
    # Load the careers data from a CSV file
    careers = pd.read_csv('careers.csv')
    return careers

def career_exploration_tool():
    st.title("Career Exploration Tool")
    st.write("Explore potential careers based on your interests and skills.")

    # Load career data
    careers = load_career_data()

    # User inputs for skills and interests
    skills = st.multiselect("Select Your Skills", options=careers['Skills'].unique())
    interests = st.multiselect("Select Your Interests", options=careers['Interests'].unique())

    if st.button("Explore Careers"):
        if not skills and not interests:
            st.warning("Please select at least one skill or interest to explore careers.")
            return

        # Filter careers based on user inputs
        try:
            filtered_careers = careers[
                careers['Skills'].apply(lambda x: any(skill in str(x) for skill in skills)) &
                careers['Interests'].apply(lambda x: any(interest in str(x) for interest in interests))
            ]
        except Exception as e:
            st.error(f"An error occurred while filtering careers: {e}")
            return

        if not filtered_careers.empty:
            st.write("### Potential Careers:")
            for _, row in filtered_careers.iterrows():
                st.write(f"**Career:** {row.get('Career', 'N/A')}")
                st.write(f"**Required Skills:** {row.get('Skills', 'N/A')}")
                st.write(f"**Interests:** {row.get('Interests', 'N/A')}")
                st.write(f"**Education Requirement:** {row.get('Education_Requirement', 'N/A')}")
                st.write(f"**Job Prospects:** {row.get('Job_Prospects', 'N/A')}")
                st.write("---")
        else:
            st.write("No careers found based on your selected skills and interests.")


